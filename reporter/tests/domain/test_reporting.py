from domain.reporting.reporter import RGReporter, RGCollectorInterface, QueueInterface
from domain.rule_group import RuleGroup, SecurityGroup
from unittest import TestCase
from unittest.mock import Mock
from random import randint


class MockQueue(Mock):
    def get_name(self):
        return "Mock Queue"

    def push(self, rg):
        print(f"{rg} pushed to {self.get_name()}")

class MockRGCollector(RGCollectorInterface, Mock):
    
    def get_name(self)->str:
        return "Mock Collector"

    def get_key(self):
        return "mock-collector"

    def get_unused_rule_groups(self) -> list:
        return [RuleGroup(f"Mock-rg-{n}", f"rg-{randint(10000,99999)}",self.get_key) for n in range(0,10)]
        

class TestRGReporter(TestCase):

    def test_report_unused_sg(self):
        mock_queue = Mock()
        mock_collector = Mock()
        rgs = [RuleGroup(f"Mock-rg-{n}", f"rg-{randint(10000,99999)}","mock-collector") for n in range(0,10)] 
        mock_collector.get_unused_rule_groups.return_value = rgs
        reporter = RGReporter(mock_queue, [mock_collector], {})
        reporter.report_unused_rg()
        mock_collector.get_unused_rule_groups.assert_called_once()
        mock_queue.push.assert_has_calls(rgs)

    def test_report_unused_sg_denied(self):
        mock_queue = Mock()
        mock_collector = Mock()
        denied_rg1 = RuleGroup("DeniedRG-1", "rg1", "mock-collector")
        denied_rg2 = RuleGroup("DeniedRG-2", "rg2", "mock-collector")
        mock_collector.get_unused_rule_groups.return_value = [denied_rg1, denied_rg2]
        reporter = RGReporter(mock_queue, [mock_collector], {"rg1", "rg2"})
        reporter.report_unused_rg()
        mock_collector.get_unused_rule_groups.assert_called_once()
        mock_queue.push.assert_not_called()

    

class TestRuleGroups(TestCase):

    def test_rule_groups(self):
        source = 'mock-collector'
        id_range = list(range(0,100))
        rgs = [ RuleGroup(f"Mock-rg-{n}", f"rg-{id_range[randint(0,len(id_range)-1)]}",source) for n in range(0,10)] 
        rg1 = RuleGroup("1", "rg-101","mock")
        rg2 = RuleGroup("2", "rg-101","mock")
        for rg in rgs:
            self.assertIn(int(rg.get_id()[3::]),set(id_range))
            self.assertEqual(rg.get_source(), source)
        self.assertNotEqual(rgs[0].get_name(),rgs[1].get_name())
        self.assertEqual(rg1, rg2)
        self.assertNotIn(rg1, set(rgs))

    def test_security_groups(self):
        source = 'mock-collector'
        id_range = list(range(0,100))
        sg1 =SecurityGroup("1", "sg-101","mock")
        sg2 =SecurityGroup("2", "sg-101","mock")
        sg1.set_arn("arn1")
        self.assertEqual(sg1.get_arn(), "arn1")






