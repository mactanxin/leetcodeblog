#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        return max( self.maxDepth(root.left), self.maxDepth(root.right) ) + 1
        