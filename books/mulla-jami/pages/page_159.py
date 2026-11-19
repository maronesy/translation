# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 159 (printed ١٥٨)."""

PAGE_NUMBER = 159
PRINTED_PAGE = "١٥٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "هو صحة كونه محكوما عليه بما أسند إليه، فإنك إذا قلت: «قام» علم منه أن ما يذكر بعده أمر يصح أن يحكم عليه بالقيام.",
     "en": "…is the validity of its being the subject of the judgment by what is predicated of it; for when you say “qāma” (stood), it is known from it that what is mentioned after it is something of which standing can validly be predicated."},
    {"type": "matn",
     "ar": "فإذا قلت: «رجل» فهو في قوة: «رجل موصوف بصحة الحكم عليه بالقيام».",
     "en": "So when you say “a man” (rajul), it is equivalent to: “a man qualified by the validity of standing being predicated of him.”"},
    {"type": "matn",
     "ar": "واعلم أن المهر[[١]] للكلب بالنباح المعتاد[[٢]] قد يكون خيرا[[٣]] كما إذا كان مجيء حبيب مثلا،",
     "en": "Know that what makes the dog snarl (al-muhirr) with its customary barking may be a good, as when it is, for example, the arrival of a beloved one;"},
    {"type": "matn",
     "ar": "وقد يكون شرا كما إذا كان مجيء عدو، والمهر له بنباح غير معتاد يتشاءم به، فيكون شرا لا خيرا.",
     "en": "and it may be an evil, as when it is the arrival of an enemy; whereas what makes it snarl with an uncustomary barking is taken as an ill omen, and so it is an evil, not a good."},
    {"type": "matn",
     "ar": "فعلى الأول: يصح القصر بالنسبة إلى الخير، فمعناه: «شر لا خير أهر ذا ناب».",
     "en": "On the first [case], restriction (qaṣr) with respect to the good is valid, so its meaning is: “An evil, not a good, made the fanged one snarl.”"},
    {"type": "matn",
     "ar": "وعلى الثاني: لا يصح، فيقدر وصف[[٤]] حتى يصح القصر، فيكون المعنى: «شر عظيم لا حقير أهر ذا ناب»،",
     "en": "On the second, it is not valid; so a qualifier is supplied by estimation so that the restriction becomes valid, and the meaning is: “A great evil, not a slight one, made the fanged one snarl.”"},
    {"type": "matn",
     "ar": "وهذا مثل[[٥]] يضرب لرجل قوي أدركه العجز في حادثة.",
     "en": "This is a proverb (mathal) applied to a strong man whom incapacity has overtaken in some event."},
    {"type": "matn",
     "ar": "(و) مثل قولك: («في الدار رجل») لتخصصه بتقديم الخبر؛",
     "en": "(And) as in your saying: (“In the house is a man”—fī al-dāri rajulun), because it is specified by the khabar being placed first;"},
    {"type": "matn",
     "ar": "لأنه إذا قيل: «في الدار» علم[[٦]] أن ما يذكر بعده موصوف بصحة استقراره في الدار[[٧]]، فهو في قوة التخصيص بالصفة.",
     "en": "for when “in the house” is said, it is known that what is mentioned after it is qualified by the validity of its being settled in the house; so it is equivalent to specification by an adjective."},
    {"type": "matn",
     "ar": "(و) مثل قولك: (سلام عليك[[٨]]) لتخصصه بنسبته إلى المتكلم[[٩]]؛ إذ أصله:",
     "en": "(And) as in your saying: (“Peace be upon you”—salāmun ʿalayka), because it is specified by its relation to the speaker; for its origin is:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بضم الميم وكسر الهاء وتشديد الراء اسم فاعل من الإهرار بمعنى الإنباح وتصويت الكلب،",
     "en": "With ḍamma on the mīm, kasra on the hāʾ and doubling of the rāʾ: the active participle from ihrār, in the sense of making [a dog] bark and the dog’s giving voice;"},
    {"type": "pair",
     "ar": "وهذا مأخوذ من الهندي.",
     "en": "this is taken from al-Hindī."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه مسامحة؛ إذ الهرير صوت للكلب دون نباحه على ما في الصحاح.",
     "en": "There is laxity of expression here; for harīr (snarling) is a sound of the dog other than its barking, according to what is in al-Ṣiḥāḥ."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: لا بالنسبة إلى الكلب. أما بالنسبة إليه، فشر،",
     "en": "It is said: [a good,] but not with respect to the dog; as for [what it is] with respect to it, it is an evil."},
    {"type": "pair",
     "ar": "وفيه نظر، لأنه يهر إذا رأى الحبيب للنشاط؛ لأنه يراه غير أجنبي، ونباحه إذ رأى العدو لاضطرابه حيث يراه أجنبيا.",
     "en": "This is open to consideration; for it snarls when it sees the beloved one out of liveliness, since it regards him as no stranger, while its barking when it sees the enemy is out of agitation, since it regards him as a stranger."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وقد يكتفى بجعل التنوين للتعظيم، والأول أنسب بحال هذا العلم، والثاني بعلم المعاني فلا تغفل،",
     "en": "One may suffice with taking the tanwīn as denoting magnification (taʿẓīm); the first is more suited to the concerns of this science, and the second to the science of meanings (ʿilm al-maʿānī)—so do not overlook [this]."},
    {"type": "pair",
     "ar": "فالمثال إنما يكون للمخصص بما يخصص به الفاعل إذا استعمل في نباح معتاد.",
     "en": "The example, then, is for [the indefinite] specified by that by which the agent is specified only when it is used of customary barking."},
    {"type": "pair",
     "ar": "وأما إذا استعمل في نباح غير معتاد، فالمثال للمخصص بالصفة.",
     "en": "When it is used of uncustomary barking, the example is for [the indefinite] specified by an adjective."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فتخصيص الابتداء إنما يحتاج إليه باعتبار أصل التركيب.",
     "en": "So the specification [required for] the mubtadaʾ is needed only with respect to the original construction."},
    {"type": "pair",
     "ar": "وأما باعتبار المعنى التمثيلي، فالتركيب مفيد من غير حاجة إلى تخصيص المبتدأ.",
     "en": "With respect to the proverbial (tamthīlī) meaning, the construction is informative without any need to specify the mubtadaʾ."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "جزما بخلاف ما إذا قيل: \"قائم رجل\"، فإن «قائما» يحتمل أن يكون مبتدأ. ولذلك خص بالظرف.",
     "en": "[Known] with certainty, unlike when one says “qāʾimun rajulun” (standing is a man), for “qāʾim” may be a mubtadaʾ; and for that reason he restricted [the example] to the adverbial (ẓarf)."},
    {"type": "pair",
     "ar": "وفيه بحث إذ قائم لا يحتمل أن يكون شيئا من قسمي المبتدأ.",
     "en": "This is open to discussion, since “qāʾim” [here] cannot be either of the two kinds of mubtadaʾ."},
    {"type": "pair",
     "ar": "ولك أن تقول: التخصيص بالظرف لسعته.",
     "en": "You may say: the restriction to the adverbial is because of its latitude (siʿa)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أورد عليه أن \"قائم رجل\" كذلك.",
     "en": "It has been objected against this that “qāʾimun rajulun” is likewise."},
    {"type": "pair",
     "ar": "ويمكن أن يعتذر بأن هذا سر نحوي لا يطرد اعتباره.",
     "en": "It may be excused on the ground that this is a grammatical rationale whose consideration is not uniformly applied."},
    {"type": "pair",
     "ar": "ولا يخفى أن الأولى أن يقول لتخصيصه بتقديم الخبر الظرف.",
     "en": "It is not hidden that it would have been better for him to say: “because it is specified by placing first the khabar that is an adverbial (ẓarf).”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "والمراد: كل نكرة كان مصدرا، ووقع في مقام الدعاء سواء كان من لفظه فعل كما في مثال المصنف أو لا، نحو: \"ويل لك\"،",
     "en": "What is meant is: every indefinite noun that is a maṣdar and occurs in the context of supplication (duʿāʾ), whether it has a verb from its own root, as in the author’s example, or not, as in “Woe to you” (waylun laka);"},
    {"type": "pair",
     "ar": "وسواء كان الدعاء بالمنفعة أو بالمضرة.",
     "en": "and whether the supplication is for benefit or for harm."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فيه أن هذا لا يجري في كل دعاء؛ إذ ليس معنى «ويل لك» ويلي لك؛",
     "en": "There is [an objection] here: this does not hold in every supplication; for the meaning of “waylun laka” is not “my woe [be] to you” (waylī laka);"},
    {"type": "pair",
     "ar": "لأن الويل هو الهلاك، ولا ويلك لك لعدم الفائدة بل معناه الهلاك لك.",
     "en": "for wayl is perdition; nor [is it] “your woe [be] to you,” since that would be uninformative; rather its meaning is “perdition to you.”"},
    {"type": "pair",
     "ar": "والقول بأن المراد بالويل دعاء الشر إطلاقا لاسم المسبب على",
     "en": "The claim that what is meant by wayl is a supplication for evil, applying the name of the effect to…"},
]
