import instaloader
from instaloader import Post

l = instaloader.Instaloader()

l.login("YOUR_USERNAME", "YOUR_PASSWORD")


post = Post.from_shortcode(l.context, 'https://www.instagram.com/p/B-Ox1QogwcK/?utm_source=ig_web_copy_link')
l.download_post(post, target="https://www.instagram.com/p/B-Ox1QogwcK/?utm_source=ig_web_copy_link")
