import asyncio
import httpx


async def get_headers(url):
    async with httpx.AsyncClient() as client:
        response = await client.head(url)
        return response.url, response.headers


def check_headers(url):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        url, headers = loop.run_until_complete(get_headers(url))

        # Define a list of recommended headers
        recommended_headers = ['Content-Type', 'Cache-Control', 'User-Agent']

        # Check if the recommended headers are missing
        missing_headers = [
            header for header in recommended_headers if header not in headers]

        return {
            'url': url,  # Return the final URL
            'existing_headers': headers,
            'missing_headers': missing_headers
        }
    except httpx.RequestError as e:
        return {
            'error': str(e)
        }


if __name__ == '__main__':
    # Test the code with a URL
    result = check_headers("https://amzn.eu/d/hE1ovds")
    print(result)
