# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 365 (printed ٣٦٤)."""

PAGE_NUMBER = 365
PRINTED_PAGE = "٣٦٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(أو بكونه) أي: بكون الضمير (مسندا إليه) أي: إلى ذلك الضمير (صفة جرت» from PDF p. 364.
    {"type": "matn",
     "ar": "على غير من هي) أي: تلك الصفة كائنة (له) فإنه لو لم ينفصل الضمير من هذه الصفة لزم الالتباس في بعض الصور،",
     "en": "…to other than the one whose) — that is, to whom that adjective belongs — (it is); for if the pronoun were not separated from this adjective, ambiguity would follow in some cases,"},
    {"type": "matn",
     "ar": "كما إذا قلت: «زيد عمرو ضاربه هو»، فإنه لو قيل: «زيد عمرو ضاربه» التبس على السامع أن الضارب زيد أو عمرو، بل المتبادر أنه عمرو؛ لأنه أقرب إلى الضمير المستتر،",
     "en": "as when you say “Zaydun ʿAmrun ḍāribuhu huwa” (Zayd, ʿAmr is the one striking him — he [Zayd]); for were it said “Zaydun ʿAmrun ḍāribuhu”, it would be unclear to the hearer whether the striker is Zayd or ʿAmr; indeed, what first comes to mind is that it is ʿAmr, since he is nearer to the concealed pronoun."},
    {"type": "matn",
     "ar": "بخلاف ما إذا قيل: «ضاربه هو»، فإنه لما انفصل الضمير على خلاف الظاهر[[١]] علم أن مرجعه ما هو خلاف الظاهر، وهو «زيد»، وإلا لا حاجة إليه،",
     "en": "This is unlike when it is said “ḍāribuhu huwa”: for when the pronoun is separated, contrary to the apparent [norm], it is known that its referent is what is contrary to the apparent, namely “Zayd”; otherwise there would be no need for it."},
    {"type": "matn",
     "ar": "وإذا وقع الالتباس بدون الانفصال في بعض الصور حمل عليه ما لا التباس فيه لاطراد الباب،",
     "en": "Since ambiguity arises without separation in some cases, what involves no ambiguity is treated like it, for the consistency of the rule."},
    {"type": "matn",
     "ar": "وإنما قال: «من هي له»[[٢]] لا «ما هي له» كما هو الظاهر ليكون أشمل اقتصارا على ما هو الأصل[[٣]].",
     "en": "He said “man hiya lahu” (the one to whom it belongs) and not “mā hiya lahu” (that to which it belongs), which would be more evidently [correct] as being more comprehensive, restricting himself to what is the basic case."},
    {"type": "matn",
     "ar": "(مثل: «إياك ضربت») مثال لتقديم الضمير على العامل.",
     "en": "(Such as “iyyāka ḍarabtu”) (you I struck) is an example of fronting the pronoun before the governor."},
    {"type": "matn",
     "ar": "(و«ما ضربك إلا أنا») مثال للفصل لغرض، وهو التخصيص ههنا.",
     "en": "(And “mā ḍarabaka illā anā”) (none struck you but I) is an example of separation for a purpose, which here is restriction (takhṣīṣ)."},
    {"type": "matn",
     "ar": "(و«إياك والشر») مثال لحذف العامل أي: «اتق نفسك والشر».",
     "en": "(And “iyyāka wa-l-sharra”) (beware of evil) is an example of elision of the governor, that is, “ittaqi nafsaka wa-l-sharra” (guard yourself and [beware] evil)."},
    {"type": "matn",
     "ar": "(و«أنا زيد») مثال كون العامل معنويا.",
     "en": "(And “anā Zaydun”) (I am Zayd) is an example of the governor being abstract."},
    {"type": "matn",
     "ar": "(و«ما أنت قائما») مثال كون العامل حرفا.",
     "en": "(And “mā anta qāʾiman”) (you are not standing) is an example of the governor being a particle."},
    {"type": "matn",
     "ar": "(و«هند زيد ضاربته هي») مثال الضمير الذي أسند إليه صفة جرت على غير من هي له،",
     "en": "(And “Hindun Zaydun ḍāribatuhu hiya”) (Hind, Zayd is the one she strikes — she) is an example of the pronoun to which is predicated an adjective applied to other than the one to whom it belongs;"},
    {"type": "matn",
     "ar": "فإنه أسند إليه الضاربة الجارية على «زيد» حيث وقعت خبرا له، وهي صفة لـ«هند» حيث قام الضرب بها،",
     "en": "for “al-ḍāriba” (the striker, fem.) has been predicated of it, applied to “Zayd” in that it occurs as his predicate, while it is an attribute of “Hind” in that the striking subsists in her."},
    {"type": "matn",
     "ar": "وإنما يصح ذلك إذا كان هي فاعلا لا تأكيدا، وإلا لكان داخلا في صورة الفصل لغرض التأكيد،",
     "en": "This holds only if “hiya” is an agent and not an emphasis; otherwise it would fall under the case of separation for the purpose of emphasis."},
    {"type": "matn",
     "ar": "ولكنه تأكيد لازم لا فاعل بدليل نحو: «الزيدون ضاربوهم نحن»، وروي عن الزمخشري «ضاربهم نحن»،",
     "en": "But it is a necessary emphasis, not an agent, as is shown by such as “al-Zaydūna ḍāribūhum naḥnu” (the Zayds, we are the ones striking them); and it is reported from al-Zamakhsharī [as] “ḍāribuhum naḥnu”."},
    {"type": "matn",
     "ar": "وعلى هذا يكون فاعلا كما قال، واختار بالتمثيل صورة لا لبس فيها ليثبت الحكم في صورة اللبس بالطريق الأولى.",
     "en": "On this [latter reading] it is an agent, as he said. He chose to illustrate with a case in which there is no ambiguity so that the ruling is established a fortiori in the case of ambiguity."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأولى أنه جعل انفصال الضمير علامة لرجوعه إلى ما هو خلاف الظاهر،",
     "en": "It is better [to say] that he made the separation of the pronoun a sign of its referring to what is contrary to the apparent."},
    {"type": "pair",
     "ar": "نعم وجه المناسبة بجعل الانفصال علامة أن خلاف الظاهر أولى بما هو خلاف الظاهر،",
     "en": "Indeed, the reason it is fitting to make separation the sign is that what is contrary to the apparent is more suited to what is contrary to the apparent."},
    {"type": "pair",
     "ar": "والأحسن أن المقام يقتضي الإتيان بالظاهر في مقام الالتباس، فالضمير فيه حل محل الظاهر، فكما لا يتصل الظاهر لا يتصل الضمير.",
     "en": "Better still: the situation calls for using the explicit noun where there is ambiguity, so the pronoun there has taken the place of the explicit noun; and just as the explicit noun is not joined [to it], the pronoun is not joined."},
    {"type": "pair",
     "ar": "ولا يخفى عليك أن مقتضى لما جعل جوابه ماضيا.",
     "en": "It is not hidden from you that what “lammā” requires is that its apodosis be made past."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا خفاء في أن الأولى، بل الصواب: ما هي له،",
     "en": "There is no doubt that the better, indeed the correct, [wording] is “mā hiya lahu”."},
    {"type": "pair",
     "ar": "وما ذكره من النكتة لا يسمن ولا يغني من جوع مع أن كون العقلاء أصلا في جريان الصفة عليهم ممنوع؛ إذ الأصل ما هو الأكثر.",
     "en": "The subtle point he mentioned neither nourishes nor avails against hunger; besides, that rational beings are the basic case for an adjective being applied to them is not conceded, since the basic case is what is most frequent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مع ظهور أن الحكم لا يختلف.",
     "en": "Even though it is evident that the ruling does not differ."},
]
