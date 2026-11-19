# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 557 (printed ٥٥٦)."""

PAGE_NUMBER = 557
PRINTED_PAGE = "٥٥٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the list of places where «إن» is read with kasra (item 1,
    # «ابتداء», closes PDF p. 556).
    {"type": "matn",
     "ar": "٢-(و) كسرت أيضا (بعد القول[[١]]) وما يشتق منه؛ لأن مقول القول لا يكون إلا جملة، نحو: «قال زيد: إن عمرا قائم».",
     "en": "2. (And) it is also read with kasra (after qawl, saying) and what is derived from it, because what is said (maqūl al-qawl) can only be a sentence, as in “Zayd said: inna ʿAmran qāʾimun (ʿAmr is standing)”."},
    {"type": "matn",
     "ar": "٣-(و) كسرت أيضا (بعد) الاسم (الموصول)؛ لأن صلة الموصول لا تكون إلا جملة نحو: «جاءني الذي إن أباه قائم».",
     "en": "3. (And) it is also read with kasra (after) the (relative) noun (al-ism al-mawṣūl), because the relative clause (ṣilat al-mawṣūl) can only be a sentence, as in “jāʾanī lladhī inna abāhu qāʾimun (he whose father is standing came to me)”."},
    {"type": "matn",
     "ar": "(وفتحت) «أن»:",
     "en": "(And) “anna” (is read with fatḥa):"},
    {"type": "matn",
     "ar": "١-حال كونها مع جملتها[[٢]] (فاعلة[[٣]]) نحو: «بلغني أن زيدا عالم»، لوجوب كون الفاعل مفردا.",
     "en": "1. when it, together with its clause, is (an agent, fāʿil), as in “balaghanī anna Zaydan ʿālimun (it has reached me that Zayd is learned)”, because the agent must be a single term (mufrad);"},
    {"type": "matn",
     "ar": "٢-(و) حال كونها مع جملتها (مفعولة[[٤]]) نحو: «كرهت أن زيدا شاعرا»، لوجوب كون المفعول مفردا.",
     "en": "2. (and) when it, together with its clause, is (an object, mafʿūl), as in “karihtu anna Zaydan shāʿirun (I disliked that Zayd is a poet)”, because the object must be a single term;"},
    {"type": "matn",
     "ar": "٣-(و) حال كونها مع جملتها (مبتدأة) نحو: «عندي أنك فاضل»، لوجوب كون المبتدأ مفردا.",
     "en": "3. (and) when it, together with its clause, is (a subject, mubtadaʾ), as in “ʿindī annaka fāḍilun (in my view, you are virtuous)”, because the subject must be a single term;"},
    {"type": "matn",
     "ar": "٤-(و) حال كونها مع جملتها (مضافا إليها) نحو: «أعجبني اشتهار أنك عالم»، لوجوب كون المضاف إليه مفردا.",
     "en": "4. (and) when it, together with its clause, is (the second term of a genitive construction, muḍāf ilayhi), as in “aʿjabanī shtihāru annaka ʿālimun (the renown of your being learned pleased me)”, because the muḍāf ilayhi must be a single term."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "والمراد بالقول: ما يحكى به لا القول بمعنى الاعتقاد، فإنه في حكم العلم والظن.",
     "en": "What is meant by qawl is that by which [speech] is reported, not qawl in the sense of belief (iʿtiqād), for that falls under the rule of [verbs of] knowledge and opinion."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أن في كلام المصنف تسامحا حيث جعل نفس «إن» فاعلة، ومفعولة، ومبتدأ، ومضافا إليها",
     "en": "This indicates that there is laxity of expression (tasāmuḥ) in the author’s words, since he made “inna” itself an agent, an object, a subject and a muḍāf ilayhi,"},
    {"type": "pair",
     "ar": "باعتبار أنها المصححة لصيرورة ما بعدها كذلك.",
     "en": "on the consideration that it is what validates what follows it becoming such."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: printed «ليس فعلا» where the list (فاعلة، مفعولة…) suggests «فاعلا» — transcribed as printed.
    {"type": "pair",
     "ar": "نبه على أن في كلامه مسامحة؛ لأن «أن» ليس فعلا ولا مفعولا ولا مبتدأ ولا مضافا إليه، بل هي مع جملتها أحد هذه الأشياء.",
     "en": "He has pointed out that there is laxity in his words, because “anna” is not a verb (fiʿl), nor an object, nor a subject, nor a muḍāf ilayhi; rather, it together with its clause is one of these things."},
    {"type": "pair",
     "ar": "ويحتمل أن يكون مراد المصنف كونها أحد هذه الأشياء في المعنى، بمعنى الثبوت",
     "en": "It is possible that the author meant its being one of these things in meaning, in the sense of established fact (thubūt);"},
    {"type": "pair",
     "ar": "ومعنى: عندي أنك قائم عندي ثبوت قيامك، فالمبتدأ في التحقيق هو الثبوت الذي هو مدلول «أن»، وهكذا البواقي،",
     "en": "the meaning of “ʿindī annaka qāʾimun” is “in my view is the established fact of your standing”, so the subject in truth is the established fact, which is what “anna” signifies; and likewise the rest."},
    # REVIEW: printed «غير معقول القول»; the context (and «غير مقول القول» two lines below) suggests «مقول» — transcribed as printed.
    {"type": "pair",
     "ar": "ومفعول ما لم يسم فاعله غير معقول القول مندرج في الفاعل على اصطلاح غير المصنف، ومندرج في المفعول على اصطلاحه.",
     "en": "The object of a verb whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu), other than what is said by qawl (printed: maʿqūl al-qawl), falls under the agent in the terminology of others than the author, and under the object in his terminology."},
    # REVIEW: the example «علمت أن زيدا قائم» is printed without the lām al-ibtidāʾ that the sentence describes (cf. «لقائم» in n. 4) — transcribed as printed.
    {"type": "pair",
     "ar": "والمراد بالمفعول غير مقول القول، ومفعول باب «علمت» إذا دخل في خبره لام الابتداء نحو: «علمت أن زيدا قائم»، فإنه يجب كسرها مع أنها مفعوله،",
     "en": "What is meant by the object is other than what is said by qawl, and [other than] the object of the class of “ʿalimtu” (I knew) when the lām of inception (lām al-ibtidāʾ) enters its predicate, as in “ʿalimtu anna Zaydan qāʾimun”; for there it must be read with kasra, although it is its object."},
    {"type": "pair",
     "ar": "والقياس أن يستثنى من المضاف إليه ما أضيف إليه حيث لا حاجة مع ذكر المضاف إليه إلى ذكر المجرور بحرف الجر، نحو: «عجبت من أنك قائم»؛",
     "en": "The regular procedure (qiyās) would be to except from the muḍāf ilayhi that to which [something] is annexed, since, with the muḍāf ilayhi mentioned, there is no need to mention what is governed in the genitive by a preposition, as in “ʿajibtu min annaka qāʾimun (I wondered at your standing)”,"},
    {"type": "pair",
     "ar": "لأنه داخل في المضاف إليه عند المصنف، كما عرفت من تعريفه للمضاف إليه، فلم يفته ذكر المجرور بحرف الجر، كما يشعر به كلام الرضي.",
     "en": "because that is included in the muḍāf ilayhi according to the author, as you have learned from his definition of the muḍāf ilayhi; so he did not omit mention of what is governed by a preposition, as the words of al-Raḍī suggest."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: ما عدا مفعول القول بقرينة ما سبق؛ لأنهم يطلقون عليه المقول دون المفعول،",
     "en": "That is, other than the object of qawl, as indicated by what preceded; for they call it “what is said” (al-maqūl), not “the object”."},
    {"type": "pair",
     "ar": "ولا حاجة إلى تخصيصه بغير باب علمت إذا دخل في خبره لام الابتداء، نحو: علمت أن زيدا لقائم؛",
     "en": "There is no need to restrict it to other than the class of ʿalimtu when the lām of inception enters its predicate, as in “ʿalimtu inna Zaydan la-qāʾimun (I knew that Zayd is indeed standing)”,"},
    {"type": "pair",
     "ar": "لأنها مع جملتها ليست مفعولة، بل قائمة مقام المفعولين، وهما في الأصل جملة.",
     "en": "because it together with its clause is not an object; rather it stands in place of the two objects, and these are originally a sentence."},
]
