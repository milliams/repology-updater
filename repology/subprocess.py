# Copyright (C) 2016-2017 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

import subprocess


def run_subprocess(command, logger, cwd=None):
    message = 'running "{}"'.format(' '.join(command))
    if cwd is not None:
        message += ' in "{}"'.format(cwd)

    logger.log(message)

    with subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT,
                          universal_newlines=True,
                          encoding='utf-8',
                          errors='ignore',
                          cwd=cwd) as proc:
        for line in proc.stdout:
            logger.GetIndented().Log(line.strip())
        proc.wait()
        logger.log('command finished with code {}'.format(proc.returncode), logger.NOTICE if proc.returncode == 0 else logger.ERROR)
        if proc.returncode != 0:
            raise subprocess.CalledProcessError(cmd=command, returncode=proc.returncode)


def get_subprocess_output(command, logger, cwd=None):
    message = 'running "{}"'.format(' '.join(command))
    if cwd is not None:
        message += ' in "{}"'.format(cwd)

    logger.log(message)

    res = ''

    with subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT,
                          universal_newlines=True,
                          encoding='utf-8',
                          errors='ignore',
                          cwd=cwd) as proc:
        for line in proc.stdout:
            res += line
        proc.wait()
        logger.log('command finished with code {}'.format(proc.returncode), logger.NOTICE if proc.returncode == 0 else logger.ERROR)
        if proc.returncode != 0:
            raise subprocess.CalledProcessError(cmd=command, returncode=proc.returncode)

    return res
