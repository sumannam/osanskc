from pptx import Presentation

prs = Presentation('caption.pptx')
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides[0]


#slide = prs.slides.add_slide(title_slide_layout)
# title = slide.shapes.title
subtitle = slide.placeholders[1]

# title.text = "Hello,p World!"
subtitle.text = "\n python-pptx was here!"

prs.save('new-caption.pptx')
