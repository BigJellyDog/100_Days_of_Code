from PIL import Image, ImageSequence
import io


def adjust_gif_symmetry(image_path, new_path, left_margin, right_margin):
    # Open the original GIF
    with Image.open(image_path) as img:
        frames = []
        bg_frame = None

        for i, frame in enumerate(ImageSequence.Iterator(img)):
            # Convert to RGBA if necessary
            frame = frame.convert("RGBA")

            # Determine new size and create a new frame
            new_width = frame.width + (right_margin - left_margin)
            new_frame = Image.new("RGBA", (new_width, frame.height))

            # Handle disposal methods
            if i > 0:
                if img.disposal_method == 2:  # Restore to background
                    bg_frame = Image.new("RGBA", img.size, (0, 0, 0, 0))
                elif img.disposal_method == 0:  # No disposal specified
                    bg_frame = frames[-1]

            if bg_frame:
                new_frame.paste(bg_frame, (right_margin - left_margin, 0))

            new_frame.paste(frame, (right_margin - left_margin, 0), frame)

            # Append to frames and update background frame
            frames.append(new_frame)
            bg_frame = new_frame

        # Save the frames as a new GIF
        frames[0].save(new_path, save_all=True, append_images=frames[1:], loop=0, duration=img.info['duration'])


# Adjust the following parameters as needed
image_path = "lock_gif.gif"
new_path = "lock_adjusted.gif"
left_margin = 73
right_margin = 103

adjust_gif_symmetry(image_path, new_path, left_margin, right_margin)
