"""
A collection of utility definitions for convolutional operations and concepts. These depend at most on numpy.
"""
import numpy as np


def samePadding(kernelSize, dilation=1):
    """
    Return the padding value needed to ensure a convolution using the given kernel size produces an output of the same
    shape as the input for a stride of 1, otherwise ensure a shape of the input divided by the stride rounded down.
    """
    kernelSize = np.atleast_1d(kernelSize)
    padding = ((kernelSize - 1) // 2) + (dilation - 1)
    padding = tuple(int(p) for p in padding)

    return tuple(padding) if len(padding) > 1 else padding[0]


def calculateOutShape(inShape, kernelSize, stride, padding):
    """
    Calculate the output tensor shape when applying a convolution to a tensor of shape `inShape' with kernel size 
    'kernelSize', stride value `stride', and input padding value `padding'. All arguments can be scalars or multiple
    values, return value is a scalar if all inputs are scalars.
    """
    inShape = np.atleast_1d(inShape)
    outShape = ((inShape - kernelSize + padding + padding) // stride) + 1
    outShape = tuple(int(s) for s in outShape)

    return tuple(outShape) if len(outShape) > 1 else outShape[0]


def oneHot(labels, numClasses):
    """
    Converts label image `labels' to a one-hot vector with `numClasses' number of channels as last dimension.
    """
    labels = labels % numClasses
    y = np.eye(numClasses)
    onehot = y[labels.flatten()]

    return onehot.reshape(tuple(labels.shape) + (numClasses,)).astype(labels.dtype)