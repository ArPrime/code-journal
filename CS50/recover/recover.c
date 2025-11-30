#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

   // Counter for the number of JPEGs found
    int jpeg_count = 0;

    // File pointer for the current JPEG
    FILE *img = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Check if the block is the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If a JPEG is already open, close it
            if (img != NULL)
            {
                fclose(img);
            }

            // Create a new filename (e.g., 000.jpg, 001.jpg)
            char filename[8];
            sprintf(filename, "%03i.jpg", jpeg_count);

            // Open a new JPEG file for writing
            img = fopen(filename, "w");
            if (img == NULL)
            {
                fclose(card);
                return 3;
            }

            // Write the buffer to the new file
            fwrite(buffer, 1, 512, img);

            // Increment the counter for the next JPEG
            jpeg_count++;
        }
        else
        {
            // If we're already writing a JPEG, continue to write to it
            if (img != NULL)
            {
                fwrite(buffer, 1, 512, img);
            }
        }
    }

    // Close the last JPEG file, if one was open
    if (img != NULL)
    {
        fclose(img);
    }

    // Close the memory card file
    fclose(card);
    return 0;
}
