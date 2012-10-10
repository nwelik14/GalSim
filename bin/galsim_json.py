"""
The main driver program for making images of galaxies whose parameters are specified
in a configuration file.
"""

import sys
import os
import galsim
import logging
import json

def main(argv):

    if len(argv) < 2: 
        print 'Usage: galsim_json config_file [ more_config_files... ]'
        sys.exit("No configuration file specified")

    # TODO: Should have a nice way of specifying a verbosity level...
    # Then we can just pass that verbosity into the logger.
    # Can also have the logging go to a file, etc.
    # We might also want to combine this with galsim_yaml and have the script 
    # either automatically (by config file extension) or explicitly (with a flag)
    # choose which kind of config files it is.
    #  -- Note: should use optparse rather than argparse, since we want it to work for 
    #           python 2.6, and we probably don't need any of the extra features that 
    #           argparse provides.
    # But for now, just do a basic setup.
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO,
        stream=sys.stdout
    )
    logger = logging.getLogger('galsim_json')

    # To turn off logging:
    #logger.propagate = False

    for config_file in argv[1:]:
        logger.info('Using config file %s',config_file)

        config = json.load(open(config_file))
        logger.info('Successfully read in config file.')

        # Set the root value
        if 'root' not in config:
            config['root'] = os.path.splitext(config_file)[0]

        # Process the configuration
        galsim.config.Process(config, logger)
    
if __name__ == "__main__":
    main(sys.argv)