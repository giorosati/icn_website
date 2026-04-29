import re

def clean_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace absolute URLs with relative
    content = content.replace('https://iowacitynotary.com/', '/')
    content = content.replace('https://iowacitynotary.com', '')

    # Remove specific feed/API links
    content = re.sub(r'<link rel="alternate" type="application/rss\+xml".*?/>', '', content)
    content = re.sub(r'<link rel="https://api\.w\.org/".*?/>', '', content)
    content = re.sub(r'<link rel="alternate" title="JSON".*?/>', '', content)
    content = re.sub(r'<link rel="EditURI".*?/>', '', content)
    content = re.sub(r'<link rel="alternate" title="oEmbed[^>]+/>', '', content)
    content = re.sub(r'<link rel="pingback"[^>]+/>', '', content)
    content = re.sub(r'<meta name="generator" content="WordPress[^>]+/>', '', content)
    content = re.sub(r'<meta content="Divi[^>]+name="generator"/>', '', content)
    
    # Remove the url-encoded query parameters for assets
    content = re.sub(r'%3Fver=[0-9.]+', '', content)
    content = re.sub(r'\?ver=[0-9.]+', '', content)
    # Generic replacement just in case
    content = re.sub(r'\?v=[0-9.]+', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    clean_html('index.html')
