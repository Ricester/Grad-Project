import requests
from bs4 import BeautifulSoup

# Function to check accessibility of a web page
def assess_accessibility(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Perform accessibility assessment logic here
        # You can use the soup object to navigate and extract relevant information
        
        # Example: Count the number of images without alt attribute
        images = soup.find_all('img')
        images_without_alt = [img for img in images if not img.has_attr('alt')]
        num_images_without_alt = len(images_without_alt)
        
        # Example: Print the assessment result
        print(f"Number of images without alt attribute: {num_images_without_alt}")
    else:
        print("Failed to retrieve the web page.")
        # Function to check if there is sufficient color contrast
        def check_color_contrast(url):
            # Send a GET request to the URL
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Perform color contrast assessment logic here
                # You can use the soup object to navigate and extract relevant information
                
                # Example: Count the number of elements with insufficient color contrast
                elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div'])
                insufficient_contrast_elements = [element for element in elements if not has_sufficient_contrast(element)]
                num_insufficient_contrast_elements = len(insufficient_contrast_elements)
                
                # Example: Print the assessment result
                print(f"Number of elements with insufficient color contrast: {num_insufficient_contrast_elements}")
            else:
                print("Failed to retrieve the web page.")

        # Function to check if an element has sufficient color contrast
        def has_sufficient_contrast(element):
            # Perform color contrast calculation logic here
            # You can use the element object to access its color properties
            
            # Example: Check if the element has sufficient contrast
            foreground_color = element.get('color')
            background_color = element.get('background-color')
            if foreground_color and background_color:
                contrast_ratio = calculate_contrast_ratio(foreground_color, background_color)
                if contrast_ratio < 4.5:
                    return False
            return True

        # Function to calculate the contrast ratio between two colors
        def calculate_contrast_ratio(color1, color2):
            # Perform contrast ratio calculation logic here
            
            # Example: Calculate the contrast ratio using the formula
            # contrast_ratio = (L1 + 0.05) / (L2 + 0.05)
            # where L1 and L2 are the relative luminance values of the colors
            # You can use color manipulation libraries like colormath or colormath to calculate relative luminance
            
            return contrast_ratio

        # Main program
        if __name__ == "__main__":
            # Enter the URL of the web page you want to assess
            url = input("Enter the URL of the web page: ")
            
            # Call the assess_accessibility function
            assess_accessibility(url)
            
            # Call the check_color_contrast function
            check_color_contrast(url)
# Main program
if __name__ == "__main__":
    # Enter the URL of the web page you want to assess
    url = input("Enter the URL of the web page: ")
    
    # Call the assess_accessibility function
    assess_accessibility(url)