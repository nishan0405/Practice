def designerPdfViewer(h, word):
    # Write your code here
    a=0
    for char in word:
        b=h[ord(char)-97]
        a=max(a,b)
    return len(word)*a
     