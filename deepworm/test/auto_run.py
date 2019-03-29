from kivy.app import App
import threading


def import_tf():
	import tensorflow as tf
	graph = tf.get_default_graph()
	print('333333333333333333333')


def load_demo():
	app.widget_manager.ids.processing_screens.current='open'
	app.widget_manager.ids.processing_screens.children[0].children[0].add_to_tree('D:\onedrive\program\worm_analyst\demo_img\elegans')
	app.widget_manager.ids.processing_screens.current='networks'
	
def load_network():
	networks=app.widget_manager.ids.processing_screens.children[0].children[0]
	networks.ids.model_spinner.text='unet'
	networks.ids.weight_spinner.text='unet.hdf5'
	print(networks.ids)

	threading.Thread(target=import_tf).start()

def auto_run():
	global app
	app=App.get_running_app()
	load_demo()
	load_network()