from nodriver import start, Config
import traceback
import pickle
import os

URL = 'https://kick.com/{}'

def save_cookies(client):
    with open("cookies.pk", "wb") as f:
        pickle.dump(client.cookies.jar._cookies, f)


def load_cookies():
    if not os.path.isfile("cookies.pk"):
        return None
    with open("cookies.pk", "rb") as f:
        return pickle.load(f)


async def fetch_new_cookies(slug):
    """Fetch new cookies using nodriver."""
    config = Config(browser_args=['--no-sandbox', '--headless',
                                  '--disable-gpu', '--disable-dev-shm-usage', '--disable-logging'],
                    no_sandbox=True)
    config.lang = 'en'
    browser = await start(config=config, lang='en', sandbox=False)
    try:
        await browser.cookies.load()
    except Exception:
        traceback.print_exc()

    tab = await browser.get(URL.format(slug))
    await tab.sleep(2)
    cookies_raw = await browser.cookies.get_all()

    cookies = {cookie.name: cookie.value for cookie in cookies_raw}
    await browser.cookies.save()
    browser.stop()

    return cookies