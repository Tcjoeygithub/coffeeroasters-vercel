#!/usr/bin/env python3
import os
import datetime
from xml.dom import minidom

def generate_sitemap(site_dir, domain):
    # Create the XML document
    doc = minidom.getDOMImplementation().createDocument(None, "urlset", None)
    root = doc.documentElement
    root.setAttribute("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Get today's date for lastmod
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Add the main pages
    main_pages = [
        {"loc": "/", "priority": "1.0", "changefreq": "weekly"},
        {"loc": "/about/", "priority": "0.8", "changefreq": "monthly"},
        {"loc": "/browse/", "priority": "0.9", "changefreq": "weekly"},
        {"loc": "/contact/", "priority": "0.7", "changefreq": "monthly"},
        {"loc": "/join/", "priority": "0.8", "changefreq": "monthly"},
        {"loc": "/privacy/", "priority": "0.5", "changefreq": "yearly"},
        {"loc": "/terms/", "priority": "0.5", "changefreq": "yearly"},
        {"loc": "/thank-you/", "priority": "0.3", "changefreq": "yearly"},
    ]
    
    for page in main_pages:
        url = doc.createElement("url")
        
        loc = doc.createElement("loc")
        loc_text = doc.createTextNode(f"{domain}{page['loc']}")
        loc.appendChild(loc_text)
        
        lastmod = doc.createElement("lastmod")
        lastmod_text = doc.createTextNode(today)
        lastmod.appendChild(lastmod_text)
        
        changefreq = doc.createElement("changefreq")
        changefreq_text = doc.createTextNode(page["changefreq"])
        changefreq.appendChild(changefreq_text)
        
        priority = doc.createElement("priority")
        priority_text = doc.createTextNode(page["priority"])
        priority.appendChild(priority_text)
        
        url.appendChild(loc)
        url.appendChild(lastmod)
        url.appendChild(changefreq)
        url.appendChild(priority)
        
        root.appendChild(url)
    
    # Add state and city pages
    for root_dir, dirs, files in os.walk(site_dir):
        # Skip the root site directory itself
        if root_dir == site_dir:
            continue
        
        # Get the relative path from the site directory
        rel_path = os.path.relpath(root_dir, site_dir)
        
        # Skip non-directory paths or special directories
        if rel_path.startswith('.') or rel_path in ['about', 'browse', 'contact', 'join', 'privacy', 'terms', 'thank-you']:
            continue
        
        # Create URL path
        url_path = f"/{rel_path}/"
        
        # Determine if it's a state or city page
        is_state = len(url_path.strip('/').split('/')) == 1
        
        url = doc.createElement("url")
        
        loc = doc.createElement("loc")
        loc_text = doc.createTextNode(f"{domain}{url_path}")
        loc.appendChild(loc_text)
        
        lastmod = doc.createElement("lastmod")
        lastmod_text = doc.createTextNode(today)
        lastmod.appendChild(lastmod_text)
        
        changefreq = doc.createElement("changefreq")
        # States change less frequently than cities
        freq = "monthly" if is_state else "monthly"
        changefreq_text = doc.createTextNode(freq)
        changefreq.appendChild(changefreq_text)
        
        priority = doc.createElement("priority")
        # States have higher priority than cities
        prio = "0.7" if is_state else "0.6"
        priority_text = doc.createTextNode(prio)
        priority.appendChild(priority_text)
        
        url.appendChild(loc)
        url.appendChild(lastmod)
        url.appendChild(changefreq)
        url.appendChild(priority)
        
        root.appendChild(url)
    
    # Write the XML to a file
    xml_str = doc.toprettyxml(indent="  ")
    with open(os.path.join(site_dir, "sitemap.xml"), "w") as f:
        f.write(xml_str)
    
    print(f"Sitemap generated at {os.path.join(site_dir, 'sitemap.xml')}")

if __name__ == "__main__":
    site_dir = "site"
    domain = "https://coffeeroasternearme.com"
    generate_sitemap(site_dir, domain) 