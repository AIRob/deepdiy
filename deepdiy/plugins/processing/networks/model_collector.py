import os,rootpath
rootpath.append(pattern='plugins')
import importlib
from utils.get_file_list import get_file_list


class ModelCollector(object):
	"""docstring for Run."""
	bundle_dir = rootpath.detect(pattern='plugins')

	def __init__(self):
		super(ModelCollector, self).__init__()
		self.models={}
		self.scan_model_zoo()

	def scan_model_zoo(self):
		self.model_names=os.listdir(self.bundle_dir+os.sep+'model_zoo')
		self.model_names=[name for name in self.model_names if name[:2]!='__']
		for name in self.model_names:
			module_name='.'.join(['model_zoo',name,'api'])
			try:module=importlib.import_module(module_name)
			except:continue
			self.models[name]=getattr(module,'Api')()
			self.models[name].config_list=get_file_list(self.bundle_dir+os.sep+'model_zoo'+os.sep+name+os.sep+'configs')
			self.models[name].weight_list=get_file_list(self.bundle_dir+os.sep+'model_zoo'+os.sep+name+os.sep+'weights')
			self.models[name].train_notebooks=get_file_list(self.bundle_dir+os.sep+'model_zoo'+os.sep+name+os.sep+'training',formats=['ipynb'])

class Test(object):
	def __init__(self,**kwargs):
		super(Test, self).__init__(**kwargs)

		mc=ModelCollector()
		print(mc.models)

if __name__ == '__main__':
	test=Test()
