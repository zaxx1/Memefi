# Contoh definisi query di queries.py

QUERY_GAME_CONFIG = """
query QUERY_GAME_CONFIG {
  telegramGameGetConfig {
    ...FragmentBossFightConfig
    __typename
  }
}

fragment FragmentBossFightConfig on TelegramGameConfigOutput {
  _id
  coinsAmount
  currentEnergy
  maxEnergy
  weaponLevel
  energyLimitLevel
  energyRechargeLevel
  tapBotLevel
  currentBoss {
    _id
    level
    currentHealth
    maxHealth
    __typename
  }
  freeBoosts {
    _id
    currentTurboAmount
    maxTurboAmount
    turboLastActivatedAt
    turboAmountLastRechargeDate
    currentRefillEnergyAmount
    maxRefillEnergyAmount
    refillEnergyLastActivatedAt
    refillEnergyAmountLastRechargeDate
    __typename
  }
  bonusLeaderDamageEndAt
  bonusLeaderDamageStartAt
  bonusLeaderDamageMultiplier
  nonce
  __typename
}
"""

# Tambahkan query-query lainnya dengan format yang sama

MUTATION_GAME_PROCESS_TAPS_BATCH = """
    mutation MutationGameProcessTapsBatch($payload: TelegramGameTapsBatchInput!) {
      telegramGameProcessTapsBatch(payload: $payload) {
        ...FragmentBossFightConfig
        __typename
      }
    }

    fragment FragmentBossFightConfig on TelegramGameConfigOutput {
      _id
      coinsAmount
      currentEnergy
      maxEnergy
      weaponLevel
      energyLimitLevel
      energyRechargeLevel
      tapBotLevel
      currentBoss {
        _id
        level
        currentHealth
        maxHealth
        __typename
      }
      freeBoosts {
        _id
        currentTurboAmount
        maxTurboAmount
        turboLastActivatedAt
        turboAmountLastRechargeDate
        currentRefillEnergyAmount
        maxRefillEnergyAmount
        refillEnergyLastActivatedAt
        refillEnergyAmountLastRechargeDate
        __typename
      }
      bonusLeaderDamageEndAt
      bonusLeaderDamageStartAt
      bonusLeaderDamageMultiplier
      nonce
      __typename
    }
    """
UPGRADE_QUERY = """
        mutation telegramGamePurchaseUpgrade($upgradeType: UpgradeType!) {
          telegramGamePurchaseUpgrade(type: $upgradeType) {
            ...FragmentBossFightConfig
            __typename
          }
        }
        fragment FragmentBossFightConfig on TelegramGameConfigOutput {
          _id
          coinsAmount
          currentEnergy
          maxEnergy
          weaponLevel
          energyLimitLevel
          energyRechargeLevel
          tapBotLevel
          currentBoss {
            _id
            level
            currentHealth
            maxHealth
            __typename
          }
          freeBoosts {
            _id
            currentTurboAmount
            maxTurboAmount
            turboLastActivatedAt
            turboAmountLastRechargeDate
            currentRefillEnergyAmount
            maxRefillEnergyAmount
            refillEnergyLastActivatedAt
            refillEnergyAmountLastRechargeDate
            __typename
          }
          bonusLeaderDamageEndAt
          bonusLeaderDamageStartAt
          bonusLeaderDamageMultiplier
          nonce
          __typename
        }
        """

QUERY_BOOSTER = """
            mutation telegramGameActivateBooster($boosterType: BoosterType!) {
              telegramGameActivateBooster(boosterType: $boosterType) {
                ...FragmentBossFightConfig
                __typename
              }
            }
            fragment FragmentBossFightConfig on TelegramGameConfigOutput {
              _id
              coinsAmount
              currentEnergy
              maxEnergy
              weaponLevel
              energyLimitLevel
              energyRechargeLevel
              tapBotLevel
              currentBoss {
                _id
                level
                currentHealth
                maxHealth
                __typename
              }
              freeBoosts {
                _id
                currentTurboAmount
                maxTurboAmount
                turboLastActivatedAt
                turboAmountLastRechargeDate
                currentRefillEnergyAmount
                maxRefillEnergyAmount
                refillEnergyLastActivatedAt
                refillEnergyAmountLastRechargeDate
                __typename
              }
              bonusLeaderDamageEndAt
              bonusLeaderDamageStartAt
              bonusLeaderDamageMultiplier
              nonce
              __typename
            }
            """

QUERY_NEXT_BOSS = """
        mutation telegramGameSetNextBoss {
          telegramGameSetNextBoss {
            ...FragmentBossFightConfig
            __typename
          }
        }
        fragment FragmentBossFightConfig on TelegramGameConfigOutput {
          _id
          coinsAmount
          currentEnergy
          maxEnergy
          weaponLevel
          energyLimitLevel
          energyRechargeLevel
          tapBotLevel
          currentBoss {
            _id
            level
            currentHealth
            maxHealth
            __typename
          }
          freeBoosts {
            _id
            currentTurboAmount
            maxTurboAmount
            turboLastActivatedAt
            turboAmountLastRechargeDate
            currentRefillEnergyAmount
            maxRefillEnergyAmount
            refillEnergyLastActivatedAt
            refillEnergyAmountLastRechargeDate
            __typename
          }
          bonusLeaderDamageEndAt
          bonusLeaderDamageStartAt
          bonusLeaderDamageMultiplier
          nonce
          __typename
        }
        """

QUERY_GET_TASK = """
        fragment FragmentCampaignTask on CampaignTaskOutput {
          id
          name
          description
          status
          type
          position
          buttonText
          coinsRewardAmount
          link
          userTaskId
          isRequired
          iconUrl
          __typename
        }

        query GetTasksList($campaignId: String!) {
          campaignTasks(campaignConfigId: $campaignId) {
            ...FragmentCampaignTask
            __typename
          }
        }
        """

QUERY_TASK_ID = """
                fragment FragmentCampaignTask on CampaignTaskOutput {
                  id
                  name
                  description
                  status
                  type
                  position
                  buttonText
                  coinsRewardAmount
                  link
                  userTaskId
                  isRequired
                  iconUrl
                  __typename
                }

                query GetTaskById($taskId: String!) {
                  campaignTaskGetConfig(taskId: $taskId) {
                    ...FragmentCampaignTask
                    __typename
                  }
                }
                """

QUERY_TASK_VERIF = """
                fragment FragmentCampaignTask on CampaignTaskOutput {
                  id
                  name
                  description
                  status
                  type
                  position
                  buttonText
                  coinsRewardAmount
                  link
                  userTaskId
                  isRequired
                  iconUrl
                  __typename
                }

                mutation CampaignTaskToVerification($userTaskId: String!) {
                  campaignTaskMoveToVerification(userTaskId: $userTaskId) {
                    ...FragmentCampaignTask
                    __typename
                  }
                }
                """

QUERY_TASK_COMPLETED = """
                fragment FragmentCampaignTask on CampaignTaskOutput {
                  id
                  name
                  description
                  status
                  type
                  position
                  buttonText
                  coinsRewardAmount
                  link
                  userTaskId
                  isRequired
                  iconUrl
                  __typename
                }

                mutation CampaignTaskCompleted($userTaskId: String!) {
                  campaignTaskMarkAsCompleted(userTaskId: $userTaskId) {
                    ...FragmentCampaignTask
                    __typename
                  }
                }
                """
QUERY_USER = """
        query QueryTelegramUserMe {
          telegramUserMe {
            firstName
            lastName
            telegramId
            username
            referralCode
            isDailyRewardClaimed
            referral {
              username
              lastName
              firstName
              bossLevel
              coinsAmount
              __typename
            }
            isReferralInitialJoinBonusAvailable
            league
            leagueIsOverTop10k
            leaguePosition
            _id
            __typename
          }
        }
        """

QUERY_LOGIN = """mutation MutationTelegramUserLogin($webAppData: TelegramWebAppDataInput!) {
            telegramUserLogin(webAppData: $webAppData) {
                access_token
                __typename
            }
        }"""

QUERY_SLOT = """fragment FragmentBossFightConfig on TelegramGameConfigOutput {
  _id
  coinsAmount
  currentEnergy
  maxEnergy
  weaponLevel
  zonesCount
  tapsReward
  energyLimitLevel
  energyRechargeLevel
  tapBotLevel
  currentBoss {
    _id
    level
    currentHealth
    maxHealth
    __typename
  }
  freeBoosts {
    _id
    currentTurboAmount
    maxTurboAmount
    turboLastActivatedAt
    turboAmountLastRechargeDate
    currentRefillEnergyAmount
    maxRefillEnergyAmount
    refillEnergyLastActivatedAt
    refillEnergyAmountLastRechargeDate
    __typename
  }
  bonusLeaderDamageEndAt
  bonusLeaderDamageStartAt
  bonusLeaderDamageMultiplier
  nonce
  spinEnergyNextRechargeAt
  spinEnergyNonRefillable
  spinEnergyRefillable
  spinEnergyTotal
  spinEnergyStaticLimit
  __typename
}

mutation spinSlotMachine($payload: SlotMachineSpinInput!) {
  slotMachineSpinV2(payload: $payload) {
    gameConfig {
      ...FragmentBossFightConfig
      __typename
    }
    spinResults {
      id
      combination
      rewardAmount
      rewardType
      questItemsFromSpin
      __typename
    }
    spinsProcessedCount
    previousProgressBarConfig {
      id
      questItem
      status
      requiredQuestItems
      collectedQuestItems
      rewardType
      rewardAmount
      questEventEndsAt
      questIndex
      questLevel
      __typename
    }
    nextProgressBarConfig {
      id
      questItem
      status
      requiredQuestItems
      collectedQuestItems
      rewardType
      rewardAmount
      questEventEndsAt
      questIndex
      questLevel
      __typename
    }
    progressBarReward {
      rewardType
      rewardAmount
      __typename
    }
    ethLotteryConfig {
      requiredItems
      collectedItems
      isCompleted
      ticketNumber
      itemsFromSpin
      maybePreviousCycleWinner {
        id
        name
        bossLevel
        ticketNumber
        rewardEth {
          currency
          amount
          __typename
        }
        rewardUsd {
          currency
          amount
          __typename
        }
        isCurrentUser
        __typename
      }
      __typename
    }
    __typename
  }
}"""

QUERY_GET_TASK_LIST = """fragment FragmentCampaignTask on CampaignTaskOutput {
  id
  name
  description
  status
  type
  position
  buttonText
  coinsRewardAmount
  spinEnergyRewardAmount
  link
  userTaskId
  isRequired
  iconUrl
  taskVerificationType
  verificationAvailableAt
  shouldUseVpn
  isLinkInternal
  quiz {
    id
    question
    answers
    __typename
  }
  __typename
}

query GetTasksList($campaignId: String!) {
  campaignTasks(campaignConfigId: $campaignId) {
    ...FragmentCampaignTask
    __typename
  }
}"""

QUERY_CAMPAIGN_TASK_VERIFICATION = """fragment FragmentCampaignTask on CampaignTaskOutput {
  id
  name
  description
  status
  type
  position
  buttonText
  coinsRewardAmount
  spinEnergyRewardAmount
  link
  userTaskId
  isRequired
  iconUrl
  taskVerificationType
  verificationAvailableAt
  shouldUseVpn
  isLinkInternal
  quiz {
    id
    question
    answers
    __typename
  }
  __typename
}

mutation CampaignTaskToVerification($taskConfigId: String!) {
  campaignTaskMoveToVerificationV2(taskConfigId: $taskConfigId) {
    ...FragmentCampaignTask
    __typename
  }
}"""

QUERY_GET_TASK_BYID = """fragment FragmentCampaignTask on CampaignTaskOutput {
  id
  name
  description
  status
  type
  position
  buttonText
  coinsRewardAmount
  spinEnergyRewardAmount
  link
  userTaskId
  isRequired
  iconUrl
  taskVerificationType
  verificationAvailableAt
  shouldUseVpn
  isLinkInternal
  quiz {
    id
    question
    answers
    __typename
  }
  __typename
}

query GetTaskById($taskId: String!) {
  campaignTaskGetConfig(taskId: $taskId) {
    ...FragmentCampaignTask
    __typename
  }
}"""

QUERY_CAMPAIGN_TASK_COMPLETE = """fragment FragmentCampaignTask on CampaignTaskOutput {
  id
  name
  description
  status
  type
  position
  buttonText
  coinsRewardAmount
  spinEnergyRewardAmount
  link
  userTaskId
  isRequired
  iconUrl
  taskVerificationType
  verificationAvailableAt
  shouldUseVpn
  isLinkInternal
  quiz {
    id
    question
    answers
    __typename
  }
  __typename
}

mutation CampaignTaskMarkAsCompleted($userTaskId: String!, $verificationCode: String, $quizAnswers: [CampaignTaskQuizQuestionInput!]) {
  campaignTaskMarkAsCompleted(
    userTaskId: $userTaskId
    verificationCode: $verificationCode
    quizAnswers: $quizAnswers
  ) {
    ...FragmentCampaignTask
    __typename
  }
}"""


QUERY_GET_CAMPAIGN_ID = """fragment FragmentCampaign on CampaignOutput {
  id
  type
  status
  backgroundImageUrl
  campaignUserParticipationId
  completedTotalTasksAmount
  description
  endDate
  iconUrl
  isStarted
  name
  completionReward {
    spinEnergyReward
    coinsReward
    claimedAt
    id
    __typename
  }
  totalRewardsPool
  totalTasksAmount
  collectedRewardsAmount
  penaltyAmount
  penaltySpinEnergyAmount
  collectedSpinEnergyRewardsAmount
  totalSpinEnergyRewardsPool
  __typename
}

query GetCampaignById($campaignId: String!) {
  campaignGetById(campaignId: $campaignId) {
    ...FragmentCampaign
    __typename
  }
}"""