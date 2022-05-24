import math

paint_boxes_count = int(input())
wallpaper_rolls_count = int(input())
gloves_price_per_pair = float(input())
brush_price = float(input())

paint_box_price = 21.50 * paint_boxes_count
wallpaper_roll_price = 5.20 * wallpaper_rolls_count

gloves_count = math.floor(0.35 * paint_boxes_count)
brush_count = math.ceil(0.48 * wallpaper_rolls_count)

all_price_gloves = gloves_count * gloves_price_per_pair
all_price_brush = brush_count * brush_price

total_sum = paint_box_price + wallpaper_roll_price + all_price_gloves + all_price_brush
delivery_price = total_sum * (1 / 15)

print(f'This delivery will cost {delivery_price:.2f} lv.')