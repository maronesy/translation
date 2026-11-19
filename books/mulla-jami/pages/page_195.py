# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 195 (printed ١٩٤)."""

PAGE_NUMBER = 195
PRINTED_PAGE = "١٩٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # REVIEW: print reads «فإنه يتعدى اللام» (one expects «باللام»); transcribed as printed.
    {"type": "matn",
     "ar": "(و) على هذا القياس (سعديك) أي: «أسعدك إسعادا بعد إسعاد» بمعنى «أعينك» إلا أن «أسعد» يتعدى بنفسه، بخلاف «ألب»، فإنه يتعدى اللام.",
     "en": "(And) on the same analogy (saʿdayka), that is: “I help you, a helping after a helping” (usʿiduka isʿādan baʿda isʿād), in the sense of “I aid you”; except that “usʿidu” is transitive by itself, unlike “ulibbu,” which takes [its object through] the lām."},

    {"type": "section", "ar": "[المفعول به]",
     "en": "The Direct Object (al-Mafʿūl Bihi)"},

    {"type": "matn",
     "ar": "(المفعول به[[١]]: هو ما وقع) أي: اسم ما وقع (عليه فعل الفاعل) ولم يذكره[[٢]] اكتفاء بما سبق في المفعول المطلق.",
     "en": "(The direct object [al-mafʿūl bihi] is what)—that is, a noun of what—(the act of the agent falls upon). He did not mention [“noun”], contenting himself with what preceded under the absolute object."},
    {"type": "matn",
     "ar": "والمراد بوقوع فعل الفاعل عليه: تعلقه به[[٣]] بلا واسطة حرف جر،",
     "en": "What is meant by the agent’s act falling upon it is its attaching to it without the mediation of a preposition;"},
    {"type": "matn",
     "ar": "فإنهم يقولون[[٤]] في «ضربت زيدا»: إن الضرب واقع على «زيد»، ولا يقولون في «مررت بزيد»[[٥]]: إن المرور واقع عليه، بل ملتبس به.",
     "en": "for they say of “ḍarabtu Zaydan” (I struck Zayd) that the striking falls upon Zayd, but they do not say of “marartu bi-Zaydin” (I passed by Zayd) that the passing falls upon him, but rather that it is connected with him."},
    {"type": "matn",
     "ar": "فخرج به المفاعيل الثلاثة الباقية، فإنه لا يقال في واحد منها: إن الفعل واقع عليه،",
     "en": "By this the three remaining objects are excluded, for it is not said of any one of them that the act falls upon it…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "اللام فيه: إما موصول، وضمير «به» راجع إليه، أي: الذي فعل به،",
     "en": "The lām (al-) in it is either a relative, with the pronoun of “bihi” referring back to it, that is: “that to which [something] was done”;"},
    {"type": "pair",
     "ar": "أو للتعريف بناء على عدم قصد الحدوث من لفظ المفعول، وضمير «به» راجع إلى موصوفه، أي الشيء المفعول به.",
     "en": "or it is the definite article, on the basis that occurrence (ḥudūth) is not intended by the word “mafʿūl,” the pronoun of “bihi” referring to what it qualifies, that is: “the thing to which [something] is done.”"},
    {"type": "pair",
     "ar": "وعلى التقديرين لفظ «المفعول» مسند إلى «به». ويجوز إسناده إلى المصدر، أي: الذي فعل فعل متعلق به أو فعل فعل بسببه،",
     "en": "On both constructions the word “mafʿūl” is predicated of “bihi.” It may also be predicated of the maṣdar, that is: “that with which an act was done in connection” or “that because of which an act was done.”"},
    {"type": "pair",
     "ar": "ويسمى به؛ لأنه تعلق به على أن يكون الباء للصلة متعلقا بالمفعول باعتبار تضمنه معنى التعلق،",
     "en": "It is so named because [the act] attached to it—the bāʾ being then a connective attached to “mafʿūl,” in that it implies the sense of attachment;"},
    {"type": "pair",
     "ar": "أو لأنه أوقع الفعل بسببه على أن يكون الباء للسببية، وسببيته باعتبار أنه محل الفعل، والمحل سبب لوجود الحال،",
     "en": "or because the act was effected by reason of it—the bāʾ being then causal; its causality is in respect of its being the locus of the act, and the locus is a cause of the existence of what inheres in it;"},
    {"type": "pair",
     "ar": "وتحقق السببية في غيره لا يقدح في وجه التسمية؛ لأنه مصحح لا مرجح.",
     "en": "and that causality also obtains in others does not impair the reason for the name, because [such a reason] makes the name valid, not preferred."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: الاسم. ولك أن تقول: لا حاجة إليه؛ لأنهم يجرون صفات المدلولات المطابقية على دوالها كما ذكر،",
     "en": "That is: [the word] “noun.” You may say: there is no need for it, because they apply the attributes of what is signified by correspondence (al-madlūlāt al-muṭābaqiyya) to the words signifying them, as was mentioned;"},
    {"type": "pair",
     "ar": "وفيه مناقشة؛ لأن أسماء الاستفهام مثلا قد يكون مفعولا به، وليس وقوع الفعل عليها من صفات مدلولاتها المطابقية، بل من صفات مدلولاتها التضمنية.",
     "en": "but this is open to dispute, because interrogative nouns, for example, may be a direct object, while the act’s falling on them is not an attribute of what they signify by correspondence, but of what they signify by implication (al-taḍammuniyya)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "نفيا أو إثباتا. والمراد تعلقه به أولا. فخرج الحال والتمييز والمستثنى.",
     "en": "Whether negatively or affirmatively. What is meant is its attaching to it primarily; so the ḥāl, the specification (tamyīz) and the excepted (mustathnā) are excluded."},
    {"type": "pair",
     "ar": "قال المصنف: المراد بوقوع فعل الفاعل عليه تعلقه بما لا يعقل إلا به. ولا يخفى أن خروج الثلاثة ظاهر.",
     "en": "The author said: what is meant by the agent’s act falling upon it is its attaching to what it cannot be conceived without. It is not hidden that the exclusion of the three is evident."},
    {"type": "pair",
     "ar": "لا يقال: ينتقض التعريف بـ«عمرو» في اشتراك «زيد وعمرو»؛ لأن نسبة الاشتراك إليهما إسناد، والإسناد لا يسمى تعلقا.",
     "en": "It is not to be said that the definition is contradicted by “ʿAmr” in “Zayd and ʿAmr shared,” because the attribution of sharing to them both is predication (isnād), and predication is not called attachment."},
    {"type": "pair",
     "ar": "ولو سلم فالمراد التعلق بغير الفاعل، و«عمرو» فاعل حقيقة وإن لم يسم فاعلا لفظا.",
     "en": "Even if it were granted, what is meant is attachment to what is other than the agent, and “ʿAmr” is in reality an agent, even if it is not called an agent in wording."},
    {"type": "pair",
     "ar": "وأما قولك: «ضارب زيد عمرا» فليس «عمرو» مما قصد جهة فاعليته، بل قصد جهة مفعوليته، أعني: تعلق الفعل به من حيث الوقوع.",
     "en": "As for your saying “Zayd fought ʿAmr” (ḍāraba Zaydun ʿAmran), “ʿAmr” is not among those whose aspect as agent is intended; rather its aspect as patient is intended, namely the act’s attaching to it by way of falling [upon it]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لما فسر وقوع فعل الفاعل على المفعول به بتعلقه به بلا واسطة حرف الجر، وفي كون هذا المعنى متبادرا منه خفاء بينه بقوله:",
     "en": "Since he explained the agent’s act falling on the direct object as its attaching to it without the mediation of a preposition, and it is unclear whether this sense is what first comes to mind from it, he made it clear by his words:"},
    {"type": "pair",
     "ar": "فإنهم يقولون يعني: أن أهل اللغة يريدون منه هذا المعنى في متعارفهم.",
     "en": "“for they say”—he means: the people of the language intend this sense by it in their customary usage."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا يقال: لا يصح إخراجه؛ لأنه مفعول به؛",
     "en": "It is not to be said: excluding it is not valid, because it is a direct object;"},
    {"type": "pair",
     "ar": "لأنا نقول: لا نسلم أنه مفعول به مطلقا غير مقيد بقيد في اصطلاحهم، بل هو مفعول به بواسطة حرف الجر. وكلامنا في المطلق. وقد صرح بذلك الشيخ الرضي.",
     "en": "for we say: we do not grant that it is a direct object absolutely, unrestricted by any qualification in their terminology; rather it is a direct object by the mediation of a preposition, and our discussion concerns the unrestricted. Shaykh al-Raḍī stated this explicitly."},
]
