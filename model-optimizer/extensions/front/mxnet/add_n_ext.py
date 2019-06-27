"""
 Copyright (c) 2018-2019 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from mo.front.extractor import FrontExtractorOp
from mo.graph.graph import Node
from mo.ops.eltwise_n import EltwiseN


class AddNExtractor(FrontExtractorOp):
    op = 'add_n'
    enabled = True

    @staticmethod
    def extract(node: Node):
        EltwiseN.update_node_stat(node, {'operation': 'sum'})
        return __class__.enabled