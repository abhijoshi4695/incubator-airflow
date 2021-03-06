# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from airflow.api.client import api_client
from airflow.api.common.experimental import trigger_dag


class Client(api_client.Client):
    def trigger_dag(self, dag_id, run_id=None, conf=None, execution_date=None):
        dr = trigger_dag.trigger_dag(dag_id=dag_id,
                                     run_id=run_id,
                                     conf=conf,
                                     execution_date=None)
        return "Created {}".format(dr)
