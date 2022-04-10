def climb(height):
    days_count = 0
    while height:
        days_left = height - 8
        new_height = days_left + 3
        days_count += 1
        height = new_height
        if days_left <= 0:
            break
    return days_count


y = climb(20)
print('Number of days  is : '+str(y)+' days')
