# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import importlib
import torch.utils.data
from data_FE.base_dataset import BaseDataset
from data_FE.face_dataset import FaceTestDataset


def create_dataloader(opt, input_images, image_list):

    instance = FaceTestDataset()
    instance.initialize(opt, input_images, image_list)
    # print("dataset [%s] of size %d was created" % (type(instance).__name__, len(instance)))
    dataloader = torch.utils.data.DataLoader(
        instance,
        batch_size=opt.batchSize,
        shuffle=not opt.serial_batches,
        num_workers=int(opt.nThreads),
        drop_last=opt.isTrain,
    )
    return dataloader
