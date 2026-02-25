#!/usr/bin/env python3
# Risk Agent - Disruption Monitoring and Risk Management

import asyncio
import logging
from typing import Dict, Any, List
from datetime import datetime, timedelta
import numpy as np

logger = logging.getLogger(__name__)


class RiskAgent:
    """
    Agent responsible for monitoring supply chain risks and disruptions
    """
    def __init__(self):
        self.risk_scores = {}
        self.disruption_history = []
        self.monitoring_cache = {}
        
    async def monitor_disruptions(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Monitor for potential supply chain disruptions
        """
        try:
            logger.info("Starting disruption monitoring")
            
            # Get risk data
            risk_data = data.get('risk', {})
            
            # Monitor geopolitical risks
            geopolitical_risks = self._monitor_geopolitical_risks(risk_data)
            
            # Monitor weather risks
            weather_risks = self._monitor_weather_risks(risk_data)
            
            # Monitor supplier risks
            supplier_risks = self._monitor_supplier_risks(risk_data)
            
            # Calculate overall risk score
            overall_risk = self._calculate_overall_risk(
                geopolitical_risks, 
                weather_risks, 
                supplier_risks
            )
            
            result = {
                'timestamp': datetime.now().isoformat(),
                'geopolitical_risks': geopolitical_risks,
                'weather_risks': weather_risks,
                'supplier_risks': supplier_risks,
                'overall_risk_score': overall_risk,
                'mitigation_actions': self._generate_mitigation_actions(overall_risk),
                'risk_alert': overall_risk > 0.7
            }
            
            logger.info("Disruption monitoring completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Error in disruption monitoring: {str(e)}")
            raise
            
    def _monitor_geopolitical_risks(self, risk_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Monitor geopolitical risks
        """
        risks = []
        
        # Simplified geopolitical risk monitoring
        for region in risk_data.get('regions', []):
            risk_score = np.random.uniform(0.1, 0.9)  # Random for demo
            
            risk = {
                'region': region,
                'risk_score': risk_score,
                'risk_type': 'geopolitical',
                'severity': self._get_severity(risk_score),
                'impact': 'medium'
            }
            
            risks.append(risk)
            
        return risks
        
    def _monitor_weather_risks(self, risk_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Monitor weather-related risks
        """
        risks = []
        
        # Simplified weather risk monitoring
        for location in risk_data.get('locations', []):
            risk_score = np.random.uniform(0.1, 0.8)  # Random for demo
            
            risk = {
                'location': location,
                'risk_score': risk_score,
                'risk_type': 'weather',
                'severity': self._get_severity(risk_score),
                'impact': 'medium'
            }
            
            risks.append(risk)
            
        return risks
        
    def _monitor_supplier_risks(self, risk_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Monitor supplier risks
        """
        risks = []
        
        # Simplified supplier risk monitoring
        for supplier in risk_data.get('suppliers', []):
            risk_score = np.random.uniform(0.1, 0.95)  # Random for demo
            
            risk = {
                'supplier_id': supplier.get('id'),
                'risk_score': risk_score,
                'risk_type': 'supplier',
                'severity': self._get_severity(risk_score),
                'impact': 'high'
            }
            
            risks.append(risk)
            
        return risks
        
    def _get_severity(self, risk_score: float) -> str:
        """
        Get severity level based on risk score
        """
        if risk_score < 0.3:
            return 'low'
        elif risk_score < 0.6:
            return 'medium'
        else:
            return 'high'
        
    def _calculate_overall_risk(self, geopolitical_risks: List[Dict[str, Any]], 
                               weather_risks: List[Dict[str, Any]], 
                               supplier_risks: List[Dict[str, Any]]) -> float:
        """
        Calculate overall supply chain risk score
        """
        # Weighted average of all risk types
        geo_weight = 0.3
        weather_weight = 0.3
        supplier_weight = 0.4
        
        geo_score = np.mean([r['risk_score'] for r in geopolitical_risks]) if geopolitical_risks else 0
        weather_score = np.mean([r['risk_score'] for r in weather_risks]) if weather_risks else 0
        supplier_score = np.mean([r['risk_score'] for r in supplier_risks]) if supplier_risks else 0
        
        overall = (geo_weight * geo_score + 
                  weather_weight * weather_score + 
                  supplier_weight * supplier_score)
        
        return overall
        
    def _generate_mitigation_actions(self, risk_score: float) -> List[str]:
        """
        Generate mitigation actions based on risk score
        """
        actions = []
        
        if risk_score > 0.8:
            actions.extend([
                'Implement emergency backup suppliers',
                'Increase safety stock levels',
                'Activate crisis management team'
            ])
        elif risk_score > 0.6:
            actions.extend([
                'Review supplier contracts',
                'Increase inventory buffers',
                'Develop contingency plans'
            ])
        elif risk_score > 0.4:
            actions.extend([
                'Monitor supplier performance',
                'Review logistics routes',
                'Update risk assessments'
            ])
        
        return actions
        
    async def get_risk_report(self) -> Dict[str, Any]:
        """
        Get detailed risk report
        """
        return {
            'report_type': 'risk_monitoring',
            'generated_at': datetime.now().isoformat(),
            'overall_risk_score': 0.65,
            'risk_alert': True,
            'mitigation_actions': ['Monitor supplier performance', 'Review logistics routes']
        }
        
    async def handle_disruption(self, disruption_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle a supply chain disruption
        """
        try:
            logger.info("Handling supply chain disruption")
            
            # Log disruption
            self.disruption_history.append({
                'disruption_id': f"DIS_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'timestamp': datetime.now().isoformat(),
                'type': disruption_data.get('type'),
                'severity': disruption_data.get('severity'),
                'impact': disruption_data.get('impact')
            })
            
            # Generate response plan
            response_plan = {
                'disruption_id': f"DIS_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'response_actions': self._generate_response_actions(disruption_data),
                'recovery_time': '5 days',
                'cost_impact': 0.12  # 12% cost impact
            }
            
            logger.info("Supply chain disruption handled successfully")
            return response_plan
            
        except Exception as e:
            logger.error(f"Error handling disruption: {str(e)}")
            raise
            
    def _generate_response_actions(self, disruption_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate response actions for disruption
        """
        actions = [
            {
                'action': 'Identify alternative suppliers',
                'priority': 'high',
                'estimated_time': '2 days'
            },
            {
                'action': 'Adjust production schedules',
                'priority': 'medium',
                'estimated_time': '3 days'
            },
            {
                'action': 'Communicate with customers',
                'priority': 'high',
                'estimated_time': '1 day'
            }
        ]
        
        return actions