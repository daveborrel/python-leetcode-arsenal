import requests
from bs4 import BeautifulSoup
import os, sys
os.system('chcp 65001 > nul')
sys.stdout.reconfigure(encoding='utf-8')

def print_secret_message(link):
    response = requests.get(link)
    response.encoding = 'utf-8'
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    if not table:
        print("No table found!")
        return

    rows = table.find_all('tr')
    
    coordinates = extract_coordinates(rows)
    
    max_x = max(coord[0] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates)
    
    # Create empty grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Fill grid with characters
    for x, y, char in coordinates:
        grid[y][x] = char
    
    for row in reversed(grid):  # Reverse the rows to flip vertically
        print(''.join(row))
    
    return grid


def extract_coordinates(rows):
    coordinates = []
    for row in rows[1:]:  # Skip first row (headers)
        cells = row.find_all(['th', 'td'])
        if len(cells) >= 3:
            try:
                x = int(cells[0].get_text(strip=True))
                char = cells[1].get_text(strip=True)
                y = int(cells[2].get_text(strip=True))
                coordinates.append((x, y, char))
            except (ValueError, IndexError):
                continue  # Skip invalid rows
    
    if not coordinates:
        print("No coordinate data found!")
        return
    
    return coordinates

LINK = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
LINK2 = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'

try:
    print_secret_message(LINK2)
except Exception as e:
    print(f"Error: {e}")