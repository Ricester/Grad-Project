import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Class to store the accessibility report
class AccessibilityReport:
    def __init__(self, url):
        self.successful = False
        self.num_images_without_alt = 0
        self.num_links = 0
        self.num_insufficient_contrast_elements = 0
        self.has_valid_heading_structure = False
        self.has_valid_link_text = False
        self.has_valid_role = False
        self.has_valid_tabindex = False
        self.has_valid_form_label = False
        self.has_valid_language_attribute = False
        self.link_has_valid_title_attribute = False
        self.title_attribute = False
        self.headings = False
        self.contrast_ratio = False
        self.num_links_with_valid_text = 0
        self.num_links_without_valid_text = 0
        self.visual_hierarchy = False
        self.num_elements_without_valid_role = 0
        self.num_elements_without_valid_tabindex = 0
        self.num_elements_without_valid_form_label = 0
        self.num_elements_without_valid_language_attribute = 0
        self.num_links_without_valid_title_attribute = 0
        self.num_elements_without_aria_label = 0
        self.url = url
        parsed = urlparse(url)
        self.base_url = parsed.netloc


soup = BeautifulSoup('<html><head><title>Test</title></head><body><h1>Heading 1</h1><p>Paragraph</p></body></html>', 'html.parser')
# Function to calculate the contrast ratio between two colors
def calculate_contrast_ratio(color1, color2):
    # Perform contrast ratio calculation logic here
    # Example: Calculate the contrast ratio using the formula
    # contrast_ratio = (L1 + 0.05) / (L2 + 0.05)
    # where L1 and L2 are the relative luminance values of the colors
    
    return 5.0
        

def has_sufficient_contrast(element):
    # Perform color contrast calculation logic here
    # You can use the element object to access its color properties
    
    foreground_color = element.get('color')
    background_color = element.get('background-color')
    if foreground_color and background_color:
        contrast_ratio = calculate_contrast_ratio(foreground_color, background_color)
        if contrast_ratio < 4.5:
            print("Element does not have sufficient color contrast:", contrast_ratio)
            return True
        else:
            print("Element has sufficient color contrast:", contrast_ratio)
            return False

 # Function to check if an element has a descriptive label
def has_descriptive_label(element):
    # Perform logic to check if the element has a descriptive label
    label = element.get('aria-label')
    if label:
        return True
    else:
        return False
    

# Function to check if an element has a valid heading structure
def has_valid_heading_structure(soup):
    # Perform logic to check if the element has a valid heading structure
    h1_headings = soup.find_all('h1')
    if len(h1_headings) < 1:
        print("Document does not have an H1 heading")
        return False
    else:
        print("Document has an H1 heading")
        return True

# Function to check if an element has a valid link text
def has_valid_link_text(element):
    # Perform logic to check if the element has a valid link text
    link_text = element.text.strip()
    if len(link_text) < 1:
        return False
    else:
        return True

# Function to count the number of links with valid text
def num_links_has_valid_link_text(soup):
    links = soup.find_all('a')
    num_links_with_valid_text = 0
    for link in links:
        if has_valid_link_text(link):
            num_links_with_valid_text += 1
    print("Number of links with valid text:", num_links_with_valid_text)
    return num_links_with_valid_text

# Function to count the number of links without valid text
def num_links_without_valid_text(soup):
    links = soup.find_all('a')
    num_links_without_valid_text = 0
    for link in links:
        if not has_valid_link_text(link):
            num_links_without_valid_text += 1
    print("Number of links without valid text:", num_links_without_valid_text)
    return num_links_without_valid_text

# Function to check if an element has a valid role
def has_valid_role(element):
    # Perform logic to check if the element has a valid role
    role = element.get('role')
    if role:
        return True
    else:
        return False

# Function to check if an element has a valid tabindex
def has_valid_tabindex(element):
    # Perform logic to check if the element has a valid tabindex
    tabindex = element.get('tabindex')
    if tabindex:
        self.has_valid_tabindex = True
    else:
        return False

# Function to check if an element has a valid form label
def has_valid_form_label(element):
    # Perform logic to check if the element has a valid form label
    form_label = element.get('aria-label')
    if form_label:
        return True
    else:
        return False

# Function to check if an element has a valid language attribute
def has_valid_language_attribute(element):
    # Perform logic to check if the element has a valid language attribute
    lang_attribute = element.get('lang')

# Function to check if a link has a valid title attribute
def has_valid_title_attribute(element):
    # Perform logic to check if the link has a valid title attribute
    title_attribute = element.get('title')
    if title_attribute:
        return True
    else:
        return False

              

# Function to check accessibility of a web page
def assess_accessibility(url):
    report = AccessibilityReport(url)
    # Send a GET request to the URL
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Error: Cannot retrieve the web page: {e}")
        return report
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        report.successful = True
        
        # Perform accessibility assessment logic here
    
        images = soup.find_all('img')
        images_without_alt = [img for img in images if not img.has_attr('alt')]
        num_images_without_alt = len(images_without_alt)
        
        print("Number of images without alt attribute: {num_images_without_alt}")
        report.num_images_without_alt = num_images_without_alt
        




        # Perform logic to count the number of images
        images = soup.find_all('img')
        num_images = len(images)
                
        print(f"Number of images: {num_images}")
        report.num_images = num_images





        # Perform logic to count the number of links
        links = soup.find_all('a')
        num_links = len(links)

        # Print the number of links
        print(f"Number of links: {num_links}")
        report.num_links = num_links



        # Perform logic to check if an element has sufficient color contrast
        elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div'])
        insufficient_contrast_elements = [element for element in elements if not has_sufficient_contrast(element)]
        num_insufficient_contrast_elements = len(insufficient_contrast_elements)
                
        print(f"Number of elements with insufficient color contrast: {num_insufficient_contrast_elements}")
        report.num_insufficient_contrast_elements = num_insufficient_contrast_elements


        # Perform logic to count the number of elements that do not have a valid role attribute
        elements = soup.find_all()
        num_elements_without_valid_role = 0
        for element in elements:
            if not has_valid_role(element):
                num_elements_without_valid_role += 1
        print(f"Number of elements without a valid role attribute: {num_elements_without_valid_role}")
        report.num_elements_without_valid_role = num_elements_without_valid_role




        # Perform logic to count the number of elements that do not have a valid tabindex attribute
        elements = soup.find_all()
        num_elements_without_valid_tabindex = 0
        for element in elements:
            if not has_valid_tabindex(element):
                num_elements_without_valid_tabindex += 1
        print(f"Number of elements without a valid tabindex attribute: {num_elements_without_valid_tabindex}")
        report.num_elements_without_valid_tabindex = num_elements_without_valid_tabindex




        # Perform logic to count the number of elements that do not have a valid form label
        elements = soup.find_all()
        num_elements_without_valid_form_label = 0
        for element in elements:
            if not has_valid_form_label(element):
                num_elements_without_valid_form_label += 1
        print(f"Number of elements without a valid form label: {num_elements_without_valid_form_label}")
        report.num_elements_without_valid_form_label = num_elements_without_valid_form_label


        # Perform logic to check if the HTML page has a clear visual hierarchy
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        if len(headings) > 1:
            report.visual_hierarchy = True
        else:
            print("HTML page does not have a clear visual hierarchy")
            report.visual_hierarchy = False

        # Perform logic to count how many elements have no valid language attribute
        elements = soup.find_all()
        num_elements_without_valid_language_attribute = 0
        for element in elements:
            if not has_valid_language_attribute(element):
                num_elements_without_valid_language_attribute += 1
        print(f"Number of elements without a valid language attribute: {num_elements_without_valid_language_attribute}")
        report.num_elements_without_valid_language_attribute = num_elements_without_valid_language_attribute

        # Perform logic to count how many links have no valid title attribute
        links = soup.find_all('a')
        num_links_without_valid_title_attribute = 0
        for link in links:
            if not has_valid_title_attribute(link):
                num_links_without_valid_title_attribute += 1
        print(f"Number of links without a valid title attribute: {num_links_without_valid_title_attribute}")
        report.num_links_without_valid_title_attribute = num_links_without_valid_title_attribute

        # Perform logic to count how many elements are missing a descriptive label
        elements = soup.find_all()
        num_elements_without_aria_label = 0
        for element in elements:
            if not has_descriptive_label(element):
                num_elements_without_aria_label += 1
        print(f"Number of elements without a valid language attribute: {num_elements_without_aria_label}")
        report.num_elements_without_aria_label = num_elements_without_aria_label

        # Perform logic to parse all inaccessible elements
        parse_inaccessible_elements_image(report, soup)
        parse_inaccessible_element_contrast(report, soup)
        parse_inaccessible_elements_role(report, soup)
        parse_inaccessible_elements_tabindex(report, soup)
        parse_inaccessible_elements_form_label(report, soup)
        parse_inaccessible_elements_language_attribute(report, soup)
        parse_inaccessible_elements_title_attribute(report, soup)
        parse_inaccessible_links_text(report, soup)
        parse_inaccessible_elements_aria(report, soup)

        report.all_issues = num_insufficient_contrast_elements + num_images_without_alt + num_elements_without_valid_form_label + num_elements_without_valid_language_attribute + num_elements_without_valid_role + num_elements_without_valid_tabindex + num_links_without_valid_title_attribute + num_elements_without_aria_label
    else:
        print("Failed to retrieve the web page.")
       

    # Return the accessibility report
    return report

def parse_inaccessible_element_contrast(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements_contrast = []
    
    # Find all elements with insufficient color contrast
    elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div'])
    for element in elements:
        if has_sufficient_contrast(element):
            continue
        inaccessible_element_contrast = {
            'tag': element.name,
            'text': element.text.strip(),
            'class': element.get('class'),
            'id': element.get('id'),
            'attributes': element.attrs
        }
        inaccessible_elements_contrast.append(inaccessible_element_contrast)

    # Update the report with the inaccessible elements
    report.inaccessible_elements_contrast = inaccessible_elements_contrast

def parse_inaccessible_elements_image(report, soup):
    # Find all images without alt attributes
    inaccessible_elements_image = []
    images = soup.find_all('img')
    for image in images:
        if image.has_attr('alt'):
            continue
        img_path = image.get('src')
        src = urljoin(report.url, img_path)
        inaccessible_element_image = {
            'tag': 'img',
            'src': src,
            'class': image.get('class'),
            'id': image.get('id'),
            'attributes': image.attrs
        }
        inaccessible_elements_image.append(inaccessible_element_image)
    
    # Update the report with the inaccessible elements
    report.inaccessible_elements_image = inaccessible_elements_image
    
def parse_inaccessible_elements_role(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements_role = []
    
    # Find all elements without a valid role attribute
    elements = soup.find_all()
    for element in elements:
        if has_valid_role(element):
            continue
        inaccessible_element_role = {
            'tag': element.name,
            'text': element.text.strip(),
            'class': element.get('class'),
            'id': element.get('id'),
            'attributes': element.attrs
        }
        inaccessible_elements_role.append(inaccessible_element_role)

    # Update the report with the inaccessible elements
    report.inaccessible_elements_role = inaccessible_elements_role

def parse_inaccessible_elements_tabindex(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements_tabindex = []
    
    # Find all elements without a valid tabindex attribute
    elements = soup.find_all()
    for element in elements:
        if has_valid_tabindex(element):
            continue
        inaccessible_element_tabindex = {
            'tag': element.name,
            'text': element.text.strip(),
            'class': element.get('class'),
            'id': element.get('id'),
            'attributes': element.attrs
        }
        inaccessible_elements_tabindex.append(inaccessible_element_tabindex)

    # Update the report with the inaccessible elements
    report.inaccessible_elements_tabindex = inaccessible_elements_tabindex

def parse_inaccessible_elements_form_label(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements_form_label = []
    
    # Find all elements without a valid form label
    elements = soup.find_all()
    for element in elements:
        if has_valid_form_label(element):
            continue
        inaccessible_element_form_label = {
            'tag': element.name,
            'text': element.text.strip(),
            'class': element.get('class'),
            'id': element.get('id'),
            'attributes': element.attrs
        }
        inaccessible_elements_form_label.append(inaccessible_element_form_label)

    # Update the report with the inaccessible elements
    report.inaccessible_elements_form_label = inaccessible_elements_form_label

def parse_inaccessible_elements_language_attribute(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements_language_attribute = []
    
    # Find all elements without a valid language attribute
    elements = soup.find_all()
    for element in elements:
        if has_valid_language_attribute(element):
            continue
        inaccessible_element_language_attribute = {
            'tag': element.name,
            'text': element.text.strip(),
            'class': element.get('class'),
            'id': element.get('id'),
            'attributes': element.attrs
        }
        inaccessible_elements_language_attribute.append(inaccessible_element_language_attribute)

    # Update the report with the inaccessible elements
    report.inaccessible_elements_language_attribute = inaccessible_elements_language_attribute

def parse_inaccessible_elements_title_attribute(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements_title_attribute = []
    
    # Find all links without a valid title attribute
    links = soup.find_all('a')
    for link in links:
        if has_valid_title_attribute(link):
            continue
        inaccessible_element_title_attribute = {
            'tag': 'a',
            'text': link.text.strip(),
            'href': link.get('href'),
            'class': link.get('class'),
            'id': link.get('id'),
            'attributes': link.attrs
        }
        inaccessible_elements_title_attribute.append(inaccessible_element_title_attribute)

    # Update the report with the inaccessible elements
    report.inaccessible_elements_title_attribute = inaccessible_elements_title_attribute

def parse_inaccessible_links_text(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_links_text = []
    
    # Find all links without valid text
    links = soup.find_all('a')
    for link in links:
        if has_valid_link_text(link):
            continue
        inaccessible_link_text = {
            'text': link.text.strip(),
            'href': link.get('href'),
            'class': link.get('class'),
            'id': link.get('id'),
            'attributes': link.attrs
        }
        inaccessible_links_text.append(inaccessible_link_text)

    # Update the report with the inaccessible elements
    report.inaccessible_links_text = inaccessible_links_text

def parse_inaccessible_elements_aria(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements_aria = []
    
    # Find all elements with no descriptive label
    # Elements that should have a descriptive label include:
    # a, header, footer, nav, main, audio, video, controls, input, select, button, textarea, aside, section, form, iframe, img
    elements = soup.find_all(['a', 'header', 'footer', 'nav', 'main', 'audio', 'video', 'controls', 'input', 'select', 'button', 'textarea', 'aside', 'section', 'form', 'iframe', 'img'])
    for element in elements:
        if has_descriptive_label(element):
            continue
        inaccessible_element_aria = {
            'tag': element.name,
            'text': element.text.strip(),
            'class': element.get('class'),
            'id': element.get('id'),
            'attributes': element.attrs
        }
        inaccessible_elements_aria.append(inaccessible_element_aria)
    # Update the report with the inaccessible elements
    report.inaccessible_elements_aria = inaccessible_elements_aria
    # Update the report with the number of elements without a descriptive label
    report.num_elements_without_aria_label = len(inaccessible_elements_aria)

# Main program
if __name__ == "__main__":
    # Enter the URL of the web page you want to assess
    url = input("Enter the URL of the web page: ")
    
    # Call the assess_accessibility function
    assess_accessibility(url)