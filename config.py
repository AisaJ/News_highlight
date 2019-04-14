class Config:
  pass


class ProdCongif(Config):
  pass


class DevConfig(Config):
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdCongif
}
