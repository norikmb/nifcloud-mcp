from pydantic import BaseModel
from datetime import datetime


class IPAddress(BaseModel):
    ip_address: str


class Filter(BaseModel):
    filter_type: str
    ip_addresses: list[IPAddress] | None = None


class InstanceState(BaseModel):
    description: str
    instance_id: str
    instance_unique_id: str
    reason_code: str
    state: str


class HealthCheck(BaseModel):
    healthy_threshold: int
    instance_states: list[InstanceState]
    interval: int
    target: str
    timeout: int
    unhealthy_threshold: int


class Instance(BaseModel):
    instance_id: str
    instance_unique_id: str


class SSLPolicy(BaseModel):
    ssl_policy_id: str
    ssl_policy_name: str


class Listener(BaseModel):
    balancing_type: int
    instance_port: int
    load_balancer_port: int
    protocol: str
    ssl_certificate_id: str | None = None
    ssl_policy: SSLPolicy | None = None


class ListenerDescription(BaseModel):
    listener: Listener


class SessionStickinessPolicy(BaseModel):
    enabled: bool
    expiration_period: int


class SorryPage(BaseModel):
    enabled: bool
    status_code: int


class Option(BaseModel):
    session_stickiness_policy: SessionStickinessPolicy
    sorry_page: SorryPage


class AppCookieStickinessPolicy(BaseModel):
    cookie_name: str
    policy_name: str


class LBCookieStickinessPolicy(BaseModel):
    cookie_expiration_period: str
    policy_name: str


class Policies(BaseModel):
    app_cookie_stickiness_policies: list[AppCookieStickinessPolicy]
    lb_cookie_stickiness_policies: list[LBCookieStickinessPolicy] | None = None


class LoadBalancerDescription(BaseModel):
    accounting_type: str
    availability_zones: list[str]
    created_time: datetime
    dns_name: str | None = None
    description: str
    filter: Filter
    health_check: HealthCheck
    instances: list[Instance]
    listener_descriptions: list[ListenerDescription]
    load_balancer_name: str
    network_volume: int
    next_month_accounting_type: str
    option: Option | None = None
    policies: Policies
    policy_type: str


class DescribeLoadBalancersResult(BaseModel):
    load_balancer_descriptions: list[LoadBalancerDescription]


class DescribeLoadBalancersResponse(BaseModel):
    describe_load_balancers_result: DescribeLoadBalancersResult
