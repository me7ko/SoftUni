title = input()
content_of_article = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content_of_article}\n</article>")

comment = input()
while comment != "end of comments":
    print(f"<div>\n    {comment}\n</div>")

    comment = input()