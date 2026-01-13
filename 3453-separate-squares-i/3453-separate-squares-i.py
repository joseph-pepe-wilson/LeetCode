class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        def area_beneath_m(sorted_squares, m):
            # function to calculate area of squares under the horizontal line
            # initialize the area beneath line at m = 0
            area_beneath = 0
            for x, y, side in sorted_squares:

                # current square is over the horizontal line; thus all next ones will be too
                if y > m:
                    break

                # ++total_area, if whole square is beneath
                if y + side <= m:
                    area_beneath += side * side
                    continue
                
                # adding available area in square that is cut by line
                x_side = side
                side = m - y
                area_beneath += side * x_side
            
            return area_beneath


        # initializing l = 0
        l, r, total_area = 0, 0, 0

        # initializing r = max top side of square
        # calculating total_area += next area
        for x, y, side in squares:
            total_area += side * side
            r = max(r, y + side)

        # res_y will need to be such that area is halved hence, target = total_area / 2
        target = total_area / 2
        res_y = 0

        # order squares by y-coord in ascending order
        sorted_squares = sorted(squares, key = lambda k: k[1])

        # binary search to find nearest y between range 0 to highest square's top side
        while r - l > 1e-6:

            # middle coordinate as float
            m = (l + r) / 2

            # area beneath current horizontal line
            area_beneath = area_beneath_m(sorted_squares, m)
            
            # store the current line as a valid ans
            res_y = m
            
            # moving pointers
            if area_beneath >= target:
                r = m
            else:
                l = m
        
        # return res_y
        return res_y