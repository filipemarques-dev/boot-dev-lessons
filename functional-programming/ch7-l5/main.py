def create_markdown_image(alt_text):
    enc_txt = '![' + alt_text + ']'
    def enclosed_url(url):
        encoded = url.replace("(", "%28").replace(")", "%29")
        enc_url = '('+ encoded + ')'
        markdown_url = enc_txt + enc_url
        def enclosed_title(title=""):
            new_markdown_url = ""
            if title != "":
                enc_title = '"' + title + '"'
                lst = list(markdown_url)
                lst.pop()
                new_markdown_url = "".join(lst)
                new_markdown_url += ' ' + enc_title + ')'
                return new_markdown_url
            else:
                return markdown_url
        return enclosed_title
    return enclosed_url