class Floor:
    def __init__(self, dimensions, images):
        self.images = images
        self.screen_dimensions = dimensions
        # Following expression assumes all images are of the same size
        self.tile_size = (dimnesion[0]//images[0].height, dimension[1]//images[0].width)

    def flash_background(self, surface):
        image_counter = 0
        for j in range(0, self.tile_size[0]):
            for i in range(0, self.tile_size[1]): 
                surface.blit(i * tile_size[0], j * tile_size[1], images[image_counter])
                if image_counter + 1 == len(self.images):
                    image_counter = 0
                else:
                    image_counter += 1
                    


