import torch  # 如果pytorch安装成功即可导入
import tensorflow as tf
tensorflow_version = tf.__version__
gpu_available = tf.test.is_gpu_available()
print('tensorflow version:',tensorflow_version, '\tGPU available:', gpu_available)
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([1.0, 2.0], name='b')
result = tf.add(a, b, name='add')
print(result)

print(torch.__version__) # 查看CUDA是否可用
print(torch.cuda.is_available()) # 查看CUDA是否可用
print(torch.cuda.device_count()) # 查看可用的CUDA数量
print(torch.version.cuda) # 查看CUDA的版本号
