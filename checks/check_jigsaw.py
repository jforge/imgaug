from __future__ import print_function, division, absolute_import
import imgaug as ia
import imgaug.augmenters as iaa
import timeit


def main():
    image = ia.quokka_square((200, 200))
    aug = iaa.Jigsaw(10, 10)

    images_aug = aug(images=[image] * 16)
    ia.imshow(ia.draw_grid(images_aug))

    gen_time = timeit.timeit(
        "iaa.generate_jigsaw_destinations(10, 10, 2, rng)",
        number=128,
        setup=(
            "import imgaug.augmenters as iaa; "
            "import imgaug.random as iarandom; "
            "rng = iarandom.RNG(0)"
        )
    )
    print("Time to generate 128x dest:", gen_time)

    destinations = iaa.generate_jigsaw_destinations(10, 10, 1, random_state=1)
    image_jig = iaa.apply_jigsaw(image, destinations)
    ia.imshow(image_jig)


if __name__ == "__main__":
    main()
