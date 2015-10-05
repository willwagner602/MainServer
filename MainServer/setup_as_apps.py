__author__ = 'wwagner'

import os

# Move HTML files to correct directory for serving
os.remove('templates/Thu2d/Thus2D.html')
os.rename('Thu2d/Thu2D.html', 'templates/Thu2d/Thus2D.html')

# Move static JS files to corect directory for serving
os.mkdir('Thu2d/static')
os.mkdir('Thu2d/static/Thu2d')
os.rename('Thu2d/Thu2D.js', 'Thu2d/static/Thu2d/Thu2D.js')
os.rename('Thu2d/two.min.js', 'Thu2d/static/Thu2d/two.min.js')
