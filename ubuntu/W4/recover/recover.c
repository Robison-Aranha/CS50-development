#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./recover image");
        return 1;
    }
    char filename[7];
    int count = -1;
    int verificador = 0;
    uint8_t data[512];
    FILE *img;
    FILE *file = fopen(argv[1], "r");
    while (fread(&data, 512, 1, file))
    {
        if (data[0] == 0xff && data[1] == 0xd8 && data[2] == 0xff && (data[3] & 0xf0) == 0xe0)
        {
            count++;
            verificador = 1;
            if (count == 0)
            {
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");
                fwrite(&data, 512, 1, img);
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");
                fwrite(&data, 512, 1, img);
            }
        }
        else
        {
            if (verificador == 1)
            {
                fwrite(&data, 512, 1, img);
            }
        }
    }
    fclose(file);
    fclose(img);
}