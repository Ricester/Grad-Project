import requests
from bs4 import BeautifulSoup

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
        self.inaccessible_elements = []
        self.visual_hierarchy = False


soup = BeautifulSoup('<html><head><title>Test</title></head><body><h1>Heading 1</h1><p>Paragraph</p></body></html>', 'html.parser')
# Function to calculate the contrast ratio between two colors
def calculate_contrast_ratio(color1, color2):
    # Perform contrast ratio calculation logic here
    # Example: Calculate the contrast ratio using the formula
    # contrast_ratio = (L1 + 0.05) / (L2 + 0.05)
    # where L1 and L2 are the relative luminance values of the colors
    # You can use color manipulation libraries like colormath or colormath to calculate relative luminance
    
    return 5.0
        

def has_sufficient_contrast(element):
    # Perform color contrast calculation logic here
    # You can use the element object to access its color properties
    
    # Example: Check if the element has sufficient contrast
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
        print("Element has a descriptive label")
        return True
    else:
        print("Element does not have a descriptive label")
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
        print("Link does not have valid text")
        return False
    else:
        print("Link has valid text")
        return True
    
def num_links_has_valid_link_text(soup):
    links = soup.find_all('a')
    num_links_with_valid_text = 0
    for link in links:
        if has_valid_link_text(link):
            num_links_with_valid_text += 1
    print("Number of links with valid text:", num_links_with_valid_text)
    return num_links_with_valid_text

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
        #print("Element has a valid role")
        return True
    else:
        #print("Element does not have a valid role")
        return False

# Function to check if an element has a valid tabindex
def has_valid_tabindex(element):
    # Perform logic to check if the element has a valid tabindex
    tabindex = element.get('tabindex')
    if tabindex:
        #print("Element has a valid tabindex")
        self.has_valid_tabindex = True
    else:
        #print("Element does not have a valid tabindex")
        return False

# Function to check if an element has a valid form label
def has_valid_form_label(element):
    # Perform logic to check if the element has a valid form label
    form_label = element.get('aria-label')
    if form_label:
       # print("Element has a valid form label")
        return True
    else:
        #print("Element does not have a valid form label")
        return False

# Function to check if an element has a valid language attribute
def has_valid_language_attribute(element):
    # Perform logic to check if the element has a valid language attribute
    lang_attribute = element.get('lang')
        #if lang_attribute:
        #print("Element has a valid language attribute")
    #   else:
        #print("Element does not have a valid language attribute")

# Function to check if a link has a valid title attribute
def has_valid_title_attribute(element):
    # Perform logic to check if the link has a valid title attribute
    title_attribute = element.get('title')
    if title_attribute:
        #print("Link has a valid title attribute")
        return True
    else:
        #print("Link does not have a valid title attribute")
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
        
        # Example: Print the assessment result
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

        
    else:
        print("Failed to retrieve the web page.")
       

    
    # Return the accessibility report
    return report

def parse_inaccessible_elements(report, soup):
    # Perform logic to parse all inaccessible elements
    inaccessible_elements = []
    
    # Find all elements with insufficient color contrast
    #elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div'])
    #for element in elements:
     #   if has_sufficient_contrast(element):
     #       continue
     #   inaccessible_element = {
     #       'tag': element.name,
    #        'text': element.text.strip(),
      #      'class': element.get('class'),
     #       'id': element.get('id'),
     #       'attributes': element.attrs
     #   }
     #   inaccessible_elements.append(inaccessible_element)

    # Find all images without alt attributes
    images = soup.find_all('img')
    for image in images:
        if image.has_attr('alt'):
            continue
        inaccessible_element = {
            'tag': 'img',
            'src': image.get('src'),
            'class': image.get('class'),
            'id': image.get('id'),
            'attributes': image.attrs
        }
        inaccessible_elements.append(inaccessible_element)
    
    # Update the report with the inaccessible elements
    report.inaccessible_elements = inaccessible_elements
    
    # Print the inaccessible elements
    print("Inaccessible Elements:")
    for element in inaccessible_elements:
        print(element)

# Main program
if __name__ == "__main__":
    # Enter the URL of the web page you want to assess
    url = input("Enter the URL of the web page: ")
    
    # Call the assess_accessibility function
    assess_accessibility(url)