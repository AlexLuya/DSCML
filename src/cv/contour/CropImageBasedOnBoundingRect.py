'''
Created on 18.03.2017

@author: alex
'''

#include <opencv\cv.h>
#include <opencv\highgui.h>
#include <opencv\ml.h>
#include <opencv\cxcore.h>

#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc/imgproc.hpp>

#include <opencv2\imgcodecs.hpp>

#include <stdio.h>
#include <stdlib.h>
#include<iostream>
using namespace cv;
using namespace std;

//khai báo biến
cv::Mat _img;        // ảnh gốc
cv::Mat _imgGray;        // ảnh xám
//hàm main

int main()
{
    _img = cv::imread("bs9.jpg");            // mở ảnh gốc
    if (_img.empty()) {                                    // hàm báo không mở được ảnh
        std::cout << "error: image not read from file\n\n";
        return(0);
    }
    cv::Mat src;
    medianBlur(_img, src, 9);

    // chuyển ảnh gốc sang ảnh xám
    cv::cvtColor(src, _imgGray, CV_BGR2GRAY);
    cv::Mat _imgGray2;
    medianBlur(_imgGray, _imgGray, 7);
    blur(_imgGray, _imgGray, Size(3, 3));
    //Canny
    cv::Mat edges;
    //dalation

    //cv::Canny(_imgGray, edges, 100, 250);
    cv::Canny(_imgGray, edges, 100, 200, 3);
    //contour
    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    findContours(edges, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));
    //mới

    int w_threshold = 190;
    int h_threshold = 140;
    vector<int> selected;
    Mat drawing = Mat::zeros(edges.size(), CV_8UC3);
    Rect R;
    for (int i = 0; i < contours.size(); i++)
    {
        Scalar color = Scalar(0, 255, 0);
        R = boundingRect(contours[i]);
        // filter contours according to their bounding box
        /*if (R.width > w_threshold && R.height > h_threshold)
        {
            selected.push_back(i);
            drawContours(drawing, contours, i, color, 2, 8, hierarchy, 0, Point());
        }*/
        if (R.width / (double)R.height>1.20 && R.width / (double)R.height < 1.48 && R.width > 200 && R.height > 100)
        {
            selected.push_back(i);
            drawContours(drawing, contours, i, color, 2, 8, hierarchy, 0, Point());
        }
    }
    //filter contour

    /// show image
    cv::imshow("Goc", _img);        // show ảnh gốc
    for (size_t i = 0; i < selected.size(); i++)
    {
        rectangle(_img, boundingRect(contours[selected[i]]), Scalar(0, 0, 255), 5);
    }
    
    cv::imshow("Xam", _imgGray);        // show ảnh xám
    cv::imshow("edges", edges);        // show ảnh Canny
    cv::imshow("contours", drawing);
    cv::imshow("detect", _img);        // show ảnh xám
    cv::waitKey(0);
    return(0);
}