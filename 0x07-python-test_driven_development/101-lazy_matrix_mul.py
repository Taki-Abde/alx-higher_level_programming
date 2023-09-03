#!/usr/bin/python3
# 101-lazy_matrix_mul.py

# Made by MEGATRON

"""Defines a matrix multiplication func using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of 2 matrices"""

    return (np.matmul(m_a, m_b))
