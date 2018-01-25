import model.settings as settings
import os
import numpy as np
import tensorflow as tf

# this class is for emotion classification
class ExpressionDetector:

    def __init__(self):


        width, height = settings.face_training_image_size
        self.input_width = 224
        self.input_height = 224
        self.input_std = 128
        self.input_mean = 128
        self.input_layer = 'input'
        self.output_layer = 'final_result'
        # load the pre trained tensor flow model
        self.model_file = os.path.join('data', 'retrained_graph.pb')
        self.graph = tf.Graph()
        self.graph_def = tf.GraphDef()
        with open(self.model_file, 'rb') as f:
            self.graph_def.ParseFromString(f.read())
        with self.graph.as_default():
            tf.import_graph_def(self.graph_def)
        # load the labels of the model
        self.label_file = os.path.join('data', 'retrained_labels.txt')
        self.labels = []
        proto_as_ascii_lines = tf.gfile.GFile(self.label_file).readlines()
        for l in proto_as_ascii_lines:
            self.labels.append(l.rstrip())
    # get tensors from a face image
    def load_tensor_from_image_file(self, file_name):
        input_name = 'file_reader'
        output_name = "normalized"
        file_reader = tf.read_file(file_name, input_name)
        image_reader = tf.image.decode_jpeg(file_reader, channels=3, name='jpeg_reader')
        float_caster = tf.cast(image_reader, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0);
        resized = tf.image.resize_bilinear(dims_expander, [self.input_height, self.input_width])
        normalized = tf.divide(tf.subtract(resized, [self.input_mean]), [self.input_std])
        sess = tf.Session()
        result = sess.run(normalized)
        return result
    # predict the emotion with the tensors.
    def test_emotion(self, file_path):
        t = self.load_tensor_from_image_file(file_path)
        input_name = "import/" + self.input_layer
        output_name = "import/" + self.output_layer
        input_operation = self.graph.get_operation_by_name(input_name)
        output_operation = self.graph.get_operation_by_name(output_name)
        with tf.Session(graph=self.graph) as sess:
            results = sess.run(output_operation.outputs[0],
                               {input_operation.outputs[0]: t})
        results = np.squeeze(results)
        top_k = results.argsort()[-5:][::-1]
        for i in top_k:
            return self.labels[i]









