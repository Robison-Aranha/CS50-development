#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float valores;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            valores = 0;
            valores = image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen;
            valores = round(valores / 3);
            image[i][j].rgbtRed = valores;
            image[i][j].rgbtBlue = valores;
            image[i][j].rgbtGreen = valores;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int verificador = 0;
    int blue[width];
    int green[width];
    int red[width];
    for (int i = 0; i < height; i++)
    {
        verificador = 0;
        for (int r = 0; r < width; r++)
        {
            blue[r] = image[i][r].rgbtBlue;
            red[r] = image[i][r].rgbtRed;
            green[r] = image[i][r].rgbtGreen;
        }
        for (int j = width - 1; j >= 0; j--)
        {
            image[i][j].rgbtRed = red[verificador];
            image[i][j].rgbtBlue = blue[verificador];
            image[i][j].rgbtGreen = green[verificador];
            verificador++;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    float valor[3];
    int quantidade;
    int valores1[height][width];
    int valores2[height][width];
    int valores3[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            valores1[i][j] = image[i][j].rgbtRed;
            valores2[i][j] = image[i][j].rgbtBlue;
            valores3[i][j] = image[i][j].rgbtGreen;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            valor[0] = 0;
            valor[1] = 0;
            valor[2] = 0;
            quantidade = 0;
            for (int h = i - 1; h <= i + 1; h++)
            {
                for (int r = j - 1; r <= j + 1; r++)
                {
                    if (h >= 0 && h < height && r >= 0 && r < width)
                    {
                        valor[0] += valores1[h][r];
                        valor[1] += valores2[h][r];
                        valor[2] += valores3[h][r];
                        quantidade++;
                    }
                }
            }
            image[i][j].rgbtRed = round(valor[0] / quantidade);
            image[i][j].rgbtBlue = round(valor[1] / quantidade);
            image[i][j].rgbtGreen = round(valor[2] / quantidade);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int count = 0;
    int valores1[height][width];
    int valores2[height][width];
    int valores3[height][width];
    int Gx[3];
    int Gy[3];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            valores1[i][j] = image[i][j].rgbtRed;
            valores2[i][j] = image[i][j].rgbtBlue;
            valores3[i][j] = image[i][j].rgbtGreen;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            for (int o = 0; o < 3; o++)
            {
                Gx[o] = 0;
                Gy[o] = 0;
            }
            for (int h = i - 1; h <= i + 1; h++)
            {
                if (h == i - 1 || h == i + 1)
                {
                    count = -1;
                }
                if (h == i)
                {
                    count = -2;
                }
                for (int r = j - 1; r <= j + 1; r++)
                {
                    if (h >= 0 && h < height && r >= 0 && r < width)
                    {
                        Gx[0] += valores1[h][r] * count;
                        Gx[1] += valores2[h][r] * count;
                        Gx[2] += valores3[h][r] * count;
                    }
                    if (h == i - 1 || h == i + 1)
                    {
                        count += 1;
                    }
                    else
                    {
                        count += 2;
                    }
                }
            }
            for (int h = j - 1; h <= j + 1; h++)
            {
                if (h == j - 1 || h == j + 1)
                {
                    count = -1;
                }
                if (h == j)
                {
                    count = -2;
                }
                for (int r = i - 1; r <= i + 1; r++)
                {
                    if (h >= 0 && h < width && r >= 0 && r < height)
                    {
                        Gy[0] += valores1[r][h] * count;
                        Gy[1] += valores2[r][h] * count;
                        Gy[2] += valores3[r][h] * count;
                    }
                    if (h == j - 1 || h == j + 1)
                    {
                        count += 1;
                    }
                    else
                    {
                        count += 2;
                    }
                }
            }
            if (sqrt((Gx[0] * Gx[0]) + (Gy[0] * Gy[0])) <= 255)
            {
                image[i][j].rgbtRed = round(sqrt((Gx[0] * Gx[0]) + (Gy[0] * Gy[0])));
            }
            else
            {
                image[i][j].rgbtRed = 255;
            }
            if (sqrt((Gx[1] * Gx[1]) + (Gy[1] * Gy[1])) <= 255)
            {
                image[i][j].rgbtBlue = round(sqrt((Gx[1] * Gx[1]) + (Gy[1] * Gy[1])));
            }
            else
            {
                image[i][j].rgbtBlue = 255;
            }
            if (sqrt((Gx[2] * Gx[2]) + (Gy[2] * Gy[2])) <= 255)
            {
                image[i][j].rgbtGreen = round(sqrt((Gx[2] * Gx[2]) + (Gy[2] * Gy[2])));
            }
            else
            {
                image[i][j].rgbtGreen = 255;
            }
        }
    }
    return;
}
