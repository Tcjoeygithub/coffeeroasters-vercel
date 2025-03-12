#!/usr/bin/env python3
import os
import re

def add_analytics_to_html_files(directory):
    # Google Analytics tag
    analytics_tag = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LVXVZV3728"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-LVXVZV3728');
</script>'''
    
    # Counter for modified files
    modified_count = 0
    
    # Walk through all files in the directory and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if the analytics tag is already present
                if 'G-LVXVZV3728' in content:
                    continue
                
                # Add the analytics tag after the meta description tag
                pattern = r'(<meta\s+content=".*?"\s+name="description".*?/>)'
                if re.search(pattern, content):
                    modified_content = re.sub(pattern, r'\1\n' + analytics_tag, content)
                    
                    # Write the modified content back to the file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(modified_content)
                    
                    modified_count += 1
                    print(f"Added analytics to: {file_path}")
                else:
                    # If no meta description tag, try to add after the viewport meta tag
                    pattern = r'(<meta\s+content="width=device-width,\s*initial-scale=1.0"\s+name="viewport".*?/>)'
                    if re.search(pattern, content):
                        modified_content = re.sub(pattern, r'\1\n' + analytics_tag, content)
                        
                        # Write the modified content back to the file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(modified_content)
                        
                        modified_count += 1
                        print(f"Added analytics to: {file_path}")
                    else:
                        # If no viewport meta tag, try to add after the title tag
                        pattern = r'(</title>)'
                        if re.search(pattern, content):
                            modified_content = re.sub(pattern, r'\1\n' + analytics_tag, content)
                            
                            # Write the modified content back to the file
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(modified_content)
                            
                            modified_count += 1
                            print(f"Added analytics to: {file_path}")
                        else:
                            print(f"Could not find insertion point in: {file_path}")
    
    print(f"\nTotal files modified: {modified_count}")

if __name__ == "__main__":
    site_dir = "site"
    add_analytics_to_html_files(site_dir) 