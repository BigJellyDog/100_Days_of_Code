from PIL import Image, ImageSequence


def adjust_gif_symmetry(src_image_path, destination_image_path, adjust_left_margin, adjust_right_margin):
    # Open the original GIF
    with Image.open(src_image_path) as img:
        frames = []
        bg_frame = None

        for i, frame in enumerate(ImageSequence.Iterator(img)):
            # Convert to RGBA if necessary
            frame = frame.convert("RGBA")

            # Determine new size and create a new frame
            new_width = frame.width + (adjust_right_margin - adjust_left_margin)
            new_frame = Image.new("RGBA", (new_width, frame.height))

            # Handle disposal methods
            disposal_method = frame.info.get('disposal', 0)
            if i > 0:
                if disposal_method == 2:  # Restore to background
                    bg_frame = Image.new("RGBA", (new_width, frame.height), (0, 0, 0, 0))
                elif disposal_method == 0 or disposal_method == 1:  # No disposal specified or do not dispose
                    if bg_frame:
                        new_frame.paste(bg_frame, (0, 0))

            new_frame.paste(frame, (adjust_right_margin - adjust_left_margin, 0), frame)

            # Append to frames
            frames.append(new_frame)

            # Update bg_frame for next iteration based on disposal method
            if disposal_method == 1 or disposal_method == 0:  # Do not dispose or no disposal specified
                bg_frame = new_frame.copy()

        # Save the frames as a new GIF
        frames[0].save(destination_image_path, save_all=True, append_images=frames[1:], loop=0,
                       duration=img.info.get('duration', 100), transparency=0, disposal=2)


# Adjust the following parameters as needed
# src_image_path = "lock_gif.gif"
# destination_image_path = "lock_adjusted.gif"
# adjust_left_margin = 73
# adjust_right_margin = 103

# adjust_gif_symmetry(src_image_path, destination_image_path, adjust_left_margin, adjust_right_margin)
