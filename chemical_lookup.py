import requests
import urllib3
import logging
from urllib.parse import quote

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Disable SSL warnings in dev (not recommended in prod)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Use a session with retry logic
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount("https://", adapter)
session.mount("http://", adapter)

# Define a global flag or pass it around if SSL verification should be skipped
# For a quick fix, we'll modify the functions to always pass verify=False
# This is NOT recommended for production environments.

def fetch_pubchem_image(name_or_cas):
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    try:
        # Pass verify=False directly to bypass SSL verification
        cid_resp = session.get(f"{base_url}/compound/name/{name_or_cas}/cids/JSON", timeout=10, verify=False)
        cid_resp.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        logger.warning(f"PubChem returned HTTP error: {http_err}")
        return None, None, None, None
    except Exception as e:
        logger.error(f"PubChem CID fetch failed: {e}")
        return None, None, None, None

    cids = cid_resp.json().get("IdentifierList", {}).get("CID", [])
    if not cids:
        logger.info("PubChem: No CID found.")
        return None, None, None, None
    cid = cids[0]

    try:
        # Pass verify=False directly to bypass SSL verification
        name_resp = session.get(f"{base_url}/compound/cid/{cid}/property/IUPACName/JSON", timeout=10, verify=False)
        name_resp.raise_for_status()
        props = name_resp.json().get("PropertyTable", {}).get("Properties", [])
        matched_name = props[0].get("IUPACName", name_or_cas) if props else name_or_cas
    except Exception:
        matched_name = name_or_cas

    encoded_name = quote(matched_name)
    image_url = f"https://cactus.nci.nih.gov/chemical/structure/{encoded_name}/image"

    return cid, image_url, "PubChem (Cactus)", matched_name

def fetch_cactus_image(name_or_cas):
    encoded_name = quote(name_or_cas)
    image_url = f"https://cactus.nci.nih.gov/chemical/structure/{encoded_name}/image"
    try:
        # Pass verify=False directly to bypass SSL verification
        resp = session.head(image_url, timeout=5, verify=False)
        if resp.status_code == 200:
            return None, image_url, "Cactus", name_or_cas
        else:
            logger.info(f"Cactus returned status {resp.status_code} for {name_or_cas}")
            return None, None, None, None
    except Exception as e:
        logger.error(f"Cactus request failed: {e}")
        return None, None, None, None

def fetch_wikidata(name_or_cas):
    search_url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbsearchentities",
        "search": name_or_cas,
        "language": "en",
        "format": "json",
        "limit": 1,
        "type": "item"
    }
    try:
        # Pass verify=False directly to bypass SSL verification
        resp = session.get(search_url, params=params, timeout=10, verify=False)
        resp.raise_for_status()
        results = resp.json().get("search", [])
        if results:
            entity = results[0]
            matched_name = entity.get("label", name_or_cas)
            wikidata_url = f"https://www.wikidata.org/wiki/{entity.get('id')}"
            return None, wikidata_url, "Wikidata", matched_name
        else:
            logger.info("Wikidata: No search results.")
            return None, None, None, None
    except Exception as e:
        logger.error(f"Wikidata fetch failed: {e}")
        return None, None, None, None

def fetch_chemical_info(name_or_cas):
    cid, image_url, source, matched_name = fetch_pubchem_image(name_or_cas)
    if cid or image_url:
        return cid, image_url, source, matched_name

    cid, image_url, source, matched_name = fetch_cactus_image(name_or_cas)
    if image_url:
        return cid, image_url, source, matched_name

    cid, image_url, source, matched_name = fetch_wikidata(name_or_cas)
    if image_url:
        return cid, image_url, source, matched_name

    return None, None, None, None
