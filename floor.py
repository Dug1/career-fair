class Floor:
    def __init__(self, dimensions, *images):
        self.images = images
        self.screen_dimensions = dimensions
        # Following expression assumes all images are of the same size
        self.tile_size = (dimensions[0]//images[0].get_height(), dimensions[1]//images[0].get_width())

    def flash_background(self, surface):
        image_counter = 0
        for j in range(0, self.tile_size[1]):
            for i in range(0, self.tile_size[0]+1): 
                surface.blit(self.images[image_counter], (i * 16, j * 16))
                if image_counter + 1 == len(self.images):
                    image_counter = 0
                else:
                    image_counter += 1