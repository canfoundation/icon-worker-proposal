from iconservice import *

TAG = 'WorkerProposal'


class WorkerProposal(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self._configuration = VarDB("configuration", db, value_type=str)
        self._prep_list = VarDB("prep_list", db, value_type=str)
        self._proposal_list = VarDB("proposal_list", db, value_type=str)
        self._proposal = DictDB("proposal", db, value_type=str)

    def on_install(self, voting_period_by_block: int, approval_pct: int) -> None:
        super().on_install()

        if voting_period_by_block < 0:
            revert("voting prediod must be possitive value")
        if approval_pct < 0 and approval_pct > 1:
            revert("approval percentage must be from 0 to 1")

        json_config = {}
        json_config['admin_addr'] = self.msg.sender
        json_config['voting_period_by_block'] = voting_period_by_block
        json_config['approval_pct'] = approval_pct

        self._configuration.set(json_dumps(json_config))

    def on_update(self) -> None:
        super().on_update()

    def search(list, item) -> bool:
        for i in range(len(list)):
            if list[i] == item:
                return True
        return False

    @eventlog(indexed=1)
    def FundTransfer(self, _by: Address, amount: int):
        pass

    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello"

    @external(readonly=True)
    def get_Configuration(self) -> str:
        return json_loads(self._configuration.get())

    @external(readonly=True)
    def get_PRep(self) -> str:
        return json_loads(self._prep_list.get())

    @external(readonly=True)
    def get_proposals(self) -> str:
        return json_loads(self._proposal_list.get())

    @external(readonly=True)
    def get_proposal(self, project_name: str) -> str:
        return json_loads(self._proposal[project_name])

    @external
    def config_System(self, voting_period_by_block: int, approval_pct: int):    

        json_config = json_loads(self._configuration.get())

        if self.msg.sender != json_config["admin_addr"]
            revert("only admin can update PRep list")

        if voting_period_by_block < 0:
            revert("voting prediod must be possitive value")
        if approval_pct < 0 and approval_pct > 1:
            revert("approval percentage must be from 0 to 1")

        json_config = {}
        json_config['admin_addr'] = self.msg.sender
        json_config['voting_period_by_block'] = voting_period_by_block
        json_config['approval_pct'] = approval_pct

        self._configuration.set(json_dumps(json_config))

    @external
    def set_PRep(self, prep_address: Address):
        json_config = json_loads(self._configuration.get())

        if self.msg.sender != json_config["admin_addr"]
            revert("only admin can update PRep list")

        json_preps = json_loads(self._prep_list.get())
        prep_list = []
        prep_list = json_preps["preps"]

        if search(prep_list, prep_address)
            revert("The PRep address already exist")

        prep_list.append(prep_address)
        json_config["preps"] = prep_list

        self._prep_list.set(json_dumps(json_config))

    @external
    def create_Proposal(self, project_name: str, amount: int, cycle_num: int, cycle_duration_by_block: int, description: str):

        json_proposals = json_loads(self._proposal_list.get())
        proposal_list = []
        proposal_list = json_proposals["proposals"]

        if search(proposal_list, project_name)
            revert("The proposal already created")

        if amount < 0:
            revert("amount must be possitive value")
        if cycle_num < 0:
            revert("cycle number must be possitive value")
        if cycle_duration_by_block < 0:
            revert("cycle duration must be possitive value")

        json_proposal = {}
        json_proposal["owner_address"] = self.msg.sender
        json_proposal["amount"] = amount
        json_proposal["cycle_num"] = cycle_num
        json_proposal["cycle_duration_by_block"] = cycle_duration_by_block
        json_proposal["current_cycle"] = 0
        json_proposal["description"] = description
        json_proposal["sponsor"] = ""
        json_proposal["voting_start_at_block"] = 0
        json_proposal["voting_end_at_block"] = 0
        json_proposal["voting_list"] = []
        json_proposal["voting_pct"] = 0

        self._proposal[project_name] = json_dumps(json_proposal)

    @external
    def sponsor_Proposal(self, project_name: str):
        json_preps = json_loads(self._prep_list.get())
        prep_list = []
        prep_list = json_preps["preps"]

        if !search(prep_list, self.msg.sender)
            revert("The requested address does not in PRep list")
        
        json_proposals = json_loads(self._proposal_list.get())
        proposal_list = []
        proposal_list = json_proposals["proposals"]

        if !search(proposal_list, project_name)
            revert("The project does not in proposal list")

        json_proposal = json_loads(self.self._proposal[project_name])
        if json_proposal["sponsor"]) != ""
            revert("The project already sponsored by a PRep")

        json_proposal["sponsor"] = self.msg.sender

        json_proposal["voting_start_at_block"] = self.block_height

        json_config = json_loads(self._configuration.get())

        json_proposal["voting_end_at_block"] = self.block_height + json_config["voting_period_by_block"]
        self._proposal[project_name] = json_dumps(json_proposal)

    @external
    def vote_Proposal(self, project_name: str, vote_status: bool):

        json_preps = json_loads(self._prep_list.get())
        prep_list = []
        prep_list = json_preps["preps"]

        if !search(prep_list, self.msg.sender)
            revert("The requested address does not in PRep list")
        
        json_proposals = json_loads(self._proposal_list.get())
        proposal_list = []
        proposal_list = json_proposals["proposals"]

        if !search(proposal_list, project_name)
            revert("The project does not in proposal list")

        json_proposal = json_loads(self.self._proposal[project_name])

        if self.block_height < json_proposal["voting_start_at_block"] &&  self.block_height > json_proposal["voting_end_at_block"]
            revert("The project not start yet or it have been ended")

        if json_proposal["sponsor"]) == ""
            revert("The project need a PRep to sponsor the proposal")
        
        if json_proposal["voting_end_at_block"]


        voting_list = json_proposal["voting_list"]

        is_voted = False
        up_vote = 0
        for i in range(len(voting_list)):

            if voting_list[i]["name"] == self.msg.sender:
                voting_list[i]["name"] = vote_status
                is_voted = True
                if vote_status == True
                    ++up_vote
            else if voting_list[i]["status"] == True
                ++up_vote

        if !is_voted
            voting_list.append({"name" = self.msg.sender, "status" = vote_status})
            if vote_status
                ++up_vote
        
        json_proposal["voting_pct"] = up_vote/len(voting_list)
        self._proposal[project_name] = json_dumps(json_proposal)

    @external
    def claim_Payment(self, project_name: str):
        json_config = json_loads(self._configuration.get())
        json_proposal = json_loads(self.self._proposal[project_name])

        if json_proposal["owner_address"] != self.msg.sender
            revert("Only owner can claim the payment")

        if self.block_height < json_proposal["voting_end_at_block"]
            revert("The project not finish the voting")

        if json_proposal["voting_pct"]) < json_config['approval_pct']
            revert("The project not enough the votes to receive payment")

        if json_proposal["current_cycle"]) >= json_proposal['cycle_num']
            revert("You already receive all payment cycles")

        
        payout = int(json_proposal['amount'] / json_proposal['cycle_num'])

        try:
            self.icx.transfer(self.msg.sender, payout)
            self.FundTransfer(self.msg.sender, payout)
        except:
            revert('Network issue in sending the payment.')

        json_proposal["current_cycle"] += 1
        self._proposal[project_name] = json_dumps(json_proposal)