style Inventory_frame is frame:
  background "#2dbd10"
  xsize 480
  ysize 240
  xalign 0.5
  yalign 0.4

style Inv_close_btn:
  xpos 450
  ypos 10

style Inv_vbox is vbox:
  xpos 20
  ypos 20
  spacing 10

style Inv_title_frame is frame:
  padding (0,10)
  background None

style Inv_title is text:
  size 30
  color Color((255, 255, 255, 255))

style Inv_section_title is text:
  size 18
  color Color((255, 255, 255, 255))

style Inv_item_name is text:
  size 12
  bold True
  color Color((216, 216, 216, 255))
  pos (0, 65)
