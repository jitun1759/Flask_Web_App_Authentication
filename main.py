'''
    Flask, Authentication, Databases & More - Python Website
    Referred video URL- https://youtu.be/dam0GPOAvVI
'''

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
