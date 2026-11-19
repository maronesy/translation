# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 149 (printed ١٤٨)."""

PAGE_NUMBER = 149
PRINTED_PAGE = "١٤٨"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[ نائب الفاعل ]",
     "en": "The Agent’s Deputy (Nāʾib al-Fāʿil)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(مفعول ما لم يسم فاعله) أي: مفعول فعل أو شبه فعل[[١]] لم يذكر فاعله،",
     "en": "(The object of [a verb] whose agent is not named—mafʿūlu mā lam yusamma fāʿiluhu), that is: the object of a verb or quasi-verb whose agent is not mentioned."},
    {"type": "matn",
     "ar": "وإنما لم يفصله عن الفاعل[[٢]]، ولم يقل: «ومنه» كما فصل المبتدأ حيث قال: «ومنها: المبتدأ» لشدة اتصاله بالفاعل[[٣]] حتى سماه بعض النحاة فاعلا",
     "en": "He did not separate it from the agent, nor say “and of them is…,” as he separated the mubtadaʾ when he said “and of them: the mubtadaʾ,” only because of how closely it is joined to the agent—so much so that some grammarians called it an agent."},
    {"type": "matn",
     "ar": "(كل مفعول[[٤]] حذف فاعله[[٥]]) أي: فاعل ذلك المفعول،",
     "en": "(It is every object whose agent has been elided—kullu mafʿūlin ḥudhifa fāʿiluhu), that is: the agent of that object;"},
    {"type": "matn",
     "ar": "وإنما أضيف إلى المفعول، لملابسة كونه فاعلا لفعل متعلق به",
     "en": "[the agent] is annexed to the object only because of the connection that it is the agent of a verb attached to it;"},
    {"type": "matn",
     "ar": "(وأقيم هو[[٦]]) أي: المفعول (مقامه) أي: مقام الفاعل في إسناد الفعل أو شبهه إليه.",
     "en": "(and it has been put—wa-uqīma huwa), that is: the object, (in its place—muqāmahu), that is: in the place of the agent, in having the verb or quasi-verb predicated of it."},
    {"type": "matn",
     "ar": "(وشرطه) أي: شرط مفعول ما لم يسم فاعله في حذف فاعله، وإقامته مقام الفاعل إذا كان عامله فعلا",
     "en": "(Its condition—wa-sharṭuhu), that is: the condition of the object of [a verb] whose agent is not named, for the elision of its agent and its being put in the agent’s place, when its governor is a verb,"},
    {"type": "matn",
     "ar": "(أن تغير صيغة الفعل إلى «فعل») أي: الماضي المجهول[[٧]] (و«يفعل») أي: المضارع المجهول،",
     "en": "(is that the form of the verb be changed to “fuʿila”—an tughayyara ṣīghatu al-fiʿli ilā fuʿila), that is: the passive past, (and “yufʿalu”), that is: the passive imperfect;"},
    {"type": "matn",
     "ar": "فيتناول مثل: «افتعل واستفعل ويفتعل ويستفعل» وغيرها من الأفعال المجهولة المزيدة فيها.",
     "en": "so it covers such as “uftuʿila,” “ustufʿila,” “yuftaʿalu” and “yustafʿalu,” and other passive verbs with augmented forms."},
    {"type": "matn",
     "ar": "(ولا يقع[[٨]]) موقع الفاعل (المفعول الثاني من) مفعولي (باب «علمت»[[٩]])؛",
     "en": "(And there does not occur) in the agent’s position (the second object of) the two objects of (the class of “ʿalimtu”—wa-lā yaqaʿu al-mafʿūlu al-thānī min bābi ʿalimtu);"},
    {"type": "matn",
     "ar": "لأنه مسند إلى المفعول الأول إسنادا تاما، فلو أسند الفعل إليه ولا يكون إسناده إلا تاما",
     "en": "because it is predicated of the first object with a complete predication; so were the verb predicated of it—and its predication can only be complete—…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأظهر الأخصر مفعول عامل لم يسم فاعله.",
     "en": "Clearer and more concise would be: “the object of a governor whose agent is not named.”"},
    {"type": "pair",
     "ar": "وبالجملة يصدق على مفعول المصدر المحذوف الفاعل على مفعول الفعل المحذوف الفاعل، نحو: اضربوا القوم، واضربا القوم، واضربي القوم، وأمثالها مما لا يحصى،",
     "en": "In short, it applies to the object of a verbal noun whose agent is elided [and] to the object of a verb whose agent is elided, as in: “Strike (pl.) the people,” “Strike (du.) the people,” “Strike (f.) the people,” and countless similar cases;"},
    {"type": "pair",
     "ar": "فهو من تخصيص اللفظ بقسم منه اصطلاحا.",
     "en": "so it is a case of restricting the expression to one division of it by technical convention."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "اعلم أن الفصل هو ترك العطف، وكان المصنف في هذا الكتاب فصل العنوانات، وهو واقع ههنا أيضا.",
     "en": "Know that separation (faṣl) is the omission of conjunction; the author in this book separates the headings, and that occurs here as well."},
    {"type": "pair",
     "ar": "وأما إيراد «منه» أو «منها» في أول عنوانات المرفوعات والمنصوبات فليس عادة له حتى يحتاج في تركه إلى نكتة،",
     "en": "As for placing “minhu” or “minhā” at the head of the headings of the nominatives and the accusatives, that is not his habit, such that omitting it would need a subtle reason (nukta);"},
    {"type": "pair",
     "ar": "بل يحتاج في إيراده على خلاف الأسلوب في قوله: ومنها المبتدأ والخبر إلى نكتة.",
     "en": "rather, it is placing it contrary to [his] manner, in his words “and of them: the mubtadaʾ and the khabar,” that needs a subtle reason."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لقيامه مقام الفاعل، واشتراكه معه في الأحكام.",
     "en": "Because it stands in the place of the agent and shares its rules."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن المنظور في التعريف الجنس لا الفرد، فلا يصح لفظ «كل» فلعله أقحم للإشعار بالطرد.",
     "en": "There is [an objection] to this: what is in view in a definition is the genus, not the individual, so the word “kull” is not valid; perhaps he inserted it to signal that [the definition] is co-extensive (al-ṭard)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بالمعنى المذكور لا الفاعل الحقيقي، فلا يرد النقض بـ«أنبت الربيع البقل»؛ لأن الفاعل بالمعنى المذكور مذكور لا محذوف.",
     "en": "In the sense mentioned [previously], not the real agent; so the counterexample “Spring made the herbage grow” (anbata al-rabīʿu al-baqla) does not apply, because the agent in the sense mentioned is stated, not elided."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أكد الضمير المستكن لئلا يتوهم إسناد الفعل إلى قوله: «مقامه»، فيلزم خلو الجملة المعطوفة على الجملة الواقعة صفة عن الضمير.",
     "en": "He reinforced the latent pronoun lest it be imagined that the verb is predicated of his word “muqāmahu,” which would entail that the sentence conjoined to the sentence serving as an adjective is devoid of a [resumptive] pronoun."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يعني: أنه أراد بالعلم أشهر أوصافه، أو أراد بالشخص جنسه. ويجوز تقدير معطوف أي: إلى فعل ونحوه.",
     "en": "He means: by the proper name he intended its best-known description, or by the individual [form] he intended its genus. It is also possible to supply an implied conjoined element, that is: “to fuʿila and the like.”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: لا يصح وقوعه لا أنه لا يقع في الاستعمال، وإلا كان الأنسب أن يقول: لم يقع،",
     "en": "That is: its occurring is not valid—not that it does not occur in usage; otherwise it would have been more fitting to say “it has not occurred,”"},
    {"type": "pair",
     "ar": "وألا يخصص الحكم بالمفعول الثالث من باب «أعلمت»؛ لأن الثاني منه أيضا لم يقع في استعمال مقام الفاعل.",
     "en": "and not to restrict the ruling to the third object of the class of “aʿlamtu”; because its second [object] too has not occurred in usage in the agent’s place."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لم يرد به أفعال القلوب كما هو المتبادر، بل كل فعل متعد إلى مفعولين هما مسند ومسند إليه، نقل أن المتأخرين جوزوا ذلك.",
     "en": "He did not mean by it the verbs of the heart (afʿāl al-qulūb), as first comes to mind, but every verb that takes two objects which are predicate and subject; it is reported that the later [grammarians] permitted that."},
]
